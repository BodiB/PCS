"""
Class to describe a train on the network
"""

from math import floor

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

        self.start = 0
        self.end = 0

        self.schedule = []
        self.departure_time = -1

        self.current_schedule_place = 0

        self.skip = False

        self.on_time = 0
        self.delayed = 0
        self.speed = 0

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

    def attach_rail(self, rail, tick):
        self.distance = 0
        self.rail = rail

        time = self.get_arrival_tick() - tick
        time = self.get_arrival_tick() - self.get_departure_tick()
        if (time > 1):
            if (len(self.schedule) - 1 > self.current_schedule_place):
                if(self.schedule[self.current_schedule_place + 1].skip):
                    self.speed = 500
            else:
                self.speed = (rail.get_length() / time - 1) + 10
        else:
            self.speed = 500
        if self.skip:
            self.speed = 500
        self.speed = min(self.speed, rail.get_speed())

        if self.speed <= 0:
            self.speed = rail.get_speed()

    def add_schedule(self, schedule, ticks):
        self.arrival_ticks = []
        self.departure_ticks = []
        self.current_schedule_place = 1
        self.schedule = schedule
        self.start = [schedule[0].station._name, schedule[0].departure]
        self.end = schedule[-1].station._name
        self.departure_time = schedule[0].departure

        current_minute = self.get_minutes(ticks)
        curr = 0
        for s in self.schedule:
            diff_in_minutes = 0
            if s.departure > current_minute:
                diff_in_minutes = s.departure + 60 - current_minute
            else:
                diff_in_minutes = s.departure - current_minute
            diff_in_ticks = diff_in_minutes * 60 / self._interval

            if curr == 0:
                self.departure_ticks.append(ticks + diff_in_ticks)
            else:
                self.departure_ticks.append(
                    ticks + diff_in_ticks)

            diff_in_minutes = 0
            if s.arrival < current_minute:
                diff_in_minutes = s.arrival + 60 - current_minute
            else:
                diff_in_minutes = s.arrival - current_minute
            diff_in_ticks = diff_in_minutes * 60 / self._interval

            if curr == 0:
                self.arrival_ticks.append(ticks + diff_in_ticks)
            else:
                self.arrival_ticks.append(
                    ticks + diff_in_ticks)

            curr += 1

    def get_arrival_tick(self):
        return self.arrival_ticks[self.current_schedule_place]

    def get_departure_tick(self):
        return self.departure_ticks[self.current_schedule_place]

    def get_target(self):
        """
        Returns the current target Timeslot
        """
        if self.schedule:
            return self.schedule[self.current_schedule_place]

    def get_next_stop(self):
        """
        Returns the next place the train will call at.
        """
        place = self.current_schedule_place
        if self.schedule:
            while self.schedule[place].skip:
                place = place + 1
            return self.schedule[place]

    def get_speed_kph(self):
        return round(self.speed / self._interval * 3.6, 1)

    def get_departure(self):
        return self.departure_time

    def get_data(self):
        previous = "NULL"
        ICD = ["Schiphol Airport", "Rotterdam Centraal"]
        type = "Sprinter"
        for check_type in self.schedule:
            if check_type.skip == True:
                type = "Intercity"
                break
        if type == "Intercity":
            for check_type in self.schedule:
                if ((check_type.station._name in ICD) and (previous in ICD)):
                    type = "Intercity Direct"
                previous = check_type.station._name
        if self.schedule[-1].station._name == "Paris-Nord" or self.schedule[0].station._name == "Paris-Nord":
            type = "Thalys"
        if self.start[0] == self.end:
            place = floor(len(self.schedule) / 2)
            if self.current_schedule_place < place:
                return [f"This train departed {self.start[0]} at {self.start[1]}", f"As {type} to {self.schedule[place].station._name}."]
            else:
                return [f"This train departed {self.start[0]} at {self.start[1]}", f"As {type} to {self.end} from {self.schedule[place].station._name}."]
        return [f"This train departed {self.start[0]} at {self.start[1]}", f"As {type} to {self.end}."]

    def get_skip(self):
        return self.skip

    def _is_on_time(self, tick):
        sec = self.get_seconds(tick)
        remainder = sec % 60 / self._interval
        return self.arrival_ticks[self.current_schedule_place] + remainder >= tick

    def simulate(self, tick):
        if self.rail:
            # self.get_arrival_tick

            self.distance += self.speed

            # train arrived at station
            if self.distance >= self.rail.get_length():
                end = self.rail.end_station
                end.add_train(self)
                if not self.schedule[self.current_schedule_place].skip:
                    if self._is_on_time(tick):
                        self.on_time += 1
                    else:
                        self.delayed += 1
                        print(f"DELAY: FROM: {self.schedule[self.current_schedule_place-1].station._name} TO: {self.schedule[self.current_schedule_place].station._name} with {tick} {self.arrival_ticks[self.current_schedule_place]} {tick - self.arrival_ticks[self.current_schedule_place]}")
                        print(f"This train departed {self.start[0]} at {self.start[1]}")

                self.rail = None
                self.departure_time = self.schedule[self.current_schedule_place].departure
                self.skip = self.schedule[self.current_schedule_place].skip
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
