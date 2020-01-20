"""
Class to describe a train on the network
"""

from simulationEntity import SimulationEntity


class Train(SimulationEntity):

    def __init__(self, load_capacity: int = 0, load_rate: int = 0):
        """
        Parameters:
        -   load_capacity: total amount of people that fit in the train
        -   load_rate: number of people per timestep that can enter or leave the train
        """
        super().__init__()
        self._max_capacity = load_capacity
        self._load_rate = load_rate
        self._current_load = 0

        self.schedule = []
        self.departure_time = -1

        self.current_schedule_place = 0

        self.on_time = 0
        self.delayed = 0

        self.rail = None

    def load(self, amount: int) -> int:
        """
        Parameters:
        -   amount: the amount of people to load

        Returns:
            amount of people that could not enter the train
        """

        if self._current_load + amount > self._max_capacity:
            temp = self._current_load + amount
            self._current_load = self._max_capacity
            return temp - self._max_capacity

        self._current_load += amount

        self.distance = 0
        return 0

    def unload(self) -> int:
        """
        Unloads the max amount of people for a given timestep
        """

        if self._current_load - self._load_rate > 0:
            self._current_load -= self._load_rate
            return self._load_rate

        temp = self._current_load
        self._current_load = 0

        return temp

    def attach_rail(self, rail):
        self.distance = 0
        self.rail = rail

    def add_schedule(self, schedule, ticks):
        self.arrival_ticks = []
        self.current_schedule_place = 1
        self.schedule = schedule
        self.departure_time = schedule[0].departure

        current_minute = self.get_minutes(ticks)
        curr = 0
        for s in self.schedule:
            diff_in_minutes = 0
            if s.arrival < current_minute:
                diff_in_minutes = s.arrival + 60 - current_minute
            else:
                diff_in_minutes = s.arrival - current_minute
            diff_in_ticks = diff_in_minutes * 60 / self._interval
            current_minute = s.departure

            if curr == 0:
                self.arrival_ticks.append(ticks + diff_in_ticks)
            else:
                self.arrival_ticks.append(
                    self.arrival_ticks[curr - 1] + diff_in_ticks)

            curr += 1

    def get_arrival_tick(self):
        return self.arrival_ticks[self.current_schedule_place]

    def get_target(self):
        """
        Returns the current target Timeslot
        """
        if self.schedule:
            return self.schedule[self.current_schedule_place]

    def get_departure(self):
        return self.departure_time

    def _is_on_time(self, tick):
        sec = self.get_seconds(tick)
        remainder = sec % 60 / self._interval
        return self.arrival_ticks[self.current_schedule_place] + remainder >= tick

    def simulate(self, tick):
        if self.rail:
            # self.get_arrival_tick
            time = self.get_arrival_tick() - tick
            self.distance += (self.rail.get_length() - self.distance) / time

            #self.distance += self.rail.get_speed()
            # train arrived at station
            if self.distance >= self.rail.get_length():
                end = self.rail.end_station
                end.add_train(self)
                if self._is_on_time(tick):
                    self.on_time += 1
                else:
                    self.delayed += 1

                self.rail = None
                self.departure_time = self.schedule[self.current_schedule_place].departure
                self.current_schedule_place += 1

                if self.current_schedule_place >= len(self.schedule):
                    self.schedule = []

    def is_terminated(self):
        return False if self.schedule else True

    def get_pos(self):
        if self.rail:
            ratio = self.distance / self.rail.get_length()

            start_x, start_y = self.rail.get_begin()
            end_x, end_y = self.rail.get_end()

            pos_x = int(start_x + ratio * (end_x - start_x))
            pos_y = int(start_y + ratio * (end_y - start_y))

            return pos_x, pos_y

        else:
            return (-100, -100)
