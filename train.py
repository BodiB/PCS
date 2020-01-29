"""
Class to describe a train on the network
"""

from math import floor
from random import uniform as random_delay

from simulationEntity import SimulationEntity


class Train(SimulationEntity):

    def __init__(self, load_capacity: int = 0, load_rate: int = 0):
        """
        Parameters:
            - load_capacity: total amount of people that fit in the train
            - load_rate: number of people per timestep that can enter or leave the train
        """
        super().__init__()
        self.start = 0
        self.end = 0

        self.schedule = []
        self.departure_time = -1

        self.current_schedule_place = 0

        self.skip = False

        self.on_time = 0
        self.delayed = 0
        self.delay = 0
        self.speed = 0

        self.rail = None

    def attach_rail(self, rail, tick):
        """
        Parameters:
            - rail: Rail entity
            - tick: Current time in ticks
        Returns:
            None
        Sets the given rail as the train's current rail.
        """
        self.distance = 0
        self.rail = rail

        time = self.get_arrival_tick() - tick

        if (time > 5):
            self.speed = (rail.get_length() / time - 5)
        else:
            self.speed = 5000
        if self.skip:
            self.speed = 5000

        self.speed += (random_delay(-self.speed, self.speed) / 30)
        self.speed = min(self.speed, rail.get_speed())

        if self.speed <= 0:
            self.speed = rail.get_speed()

    def add_schedule(self, schedule, ticks):
        """
        Parameters:
            - schedule: Timetable of the train in minutes
            - ticks: Current time in ticks
        Returns:
            None
        Sets the given schedule as the train's current schedule and updates the arrival ticks and departure ticks
        """
        self.arrival_ticks = []
        self.departure_ticks = []
        self.current_schedule_place = 1
        self.schedule = schedule
        self.start = [schedule[0].station._name, schedule[0].departure]
        self.end = schedule[-1].station._name
        self.departure_time = schedule[0].departure

        initial_departure = self.schedule[0].departure
        for s in self.schedule:
            arrival_tick = s.arrival
            departure_tick = s.departure
            if arrival_tick >= 0:
                arrival_tick = (s.arrival - initial_departure) * \
                    60 / self._interval
            if departure_tick >= 0:
                departure_tick = (
                    s.departure - initial_departure) * 60 / self._interval
            if arrival_tick == departure_tick or s.arrival < ticks:
                departure_tick += random_delay(20, 70) / self._interval
            self.arrival_ticks.append(arrival_tick + ticks)
            self.departure_ticks.append(departure_tick + ticks)

    def get_arrival_tick(self):
        """
        Parameters:
            None
        Returns:
            Tick the train has to arrive at the next station
        """
        return self.arrival_ticks[self.current_schedule_place]

    def get_departure_tick(self):
        """
        Parameters:
            None
        Returns:
            Tick on which the train should depart the station it is at
        """
        return self.departure_ticks[self.current_schedule_place - 1]

    def get_target(self):
        """
        Parameters:
            None
        Returns:
            Current target Timeslot
        """
        if self.schedule:
            return self.schedule[self.current_schedule_place]

    def get_next_stop(self):
        """
        Parameters:
            None
        Returns:
            Next place the train will call at.
        """
        place = self.current_schedule_place
        if self.schedule:
            while self.schedule[place].skip:
                place = place + 1
            return self.schedule[place]

    def get_speed_kph(self):
        """
        Parameters:
            None
        Returns:
            Speed the train is currently doing
        """
        return round(self.speed / self._interval * 3.6, 1)

    def get_departure(self):
        """
        Parameters:
            None
        Returns:
            Departure time of the train
        """
        return self.departure_time

    def get_data(self):
        """
        Parameters:
            None
        Returns:
            The data to be printed in _draw_trains.
        """
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
        """
        Parameters:
            None
        Returns:
            If the train is gonna skip the next station it passes (Intercity)
        """
        return self.skip

    def _is_on_time(self, tick):
        """
        Parameters:
            - tick: Current time in ticks
        Returns:
            If the train is on time
        """
        sec = self.get_seconds(tick)
        remainder = sec % 60 / self._interval
        return self.arrival_ticks[self.current_schedule_place] + remainder >= tick

    def simulate(self, tick):
        """
        Parameters:
            - tick: Current time in ticks
        Returns:
            None
        Runs the simulation step for the train given the current simulation tick
        If the train is on a rail, it will try to match the needed speed for the schedule, or 
        if the train is delayed, it will travel the max speed allowed on the current rail.
        """
        if self.rail:
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
        """
        Parameters:
            None
        Returns:
            If the train has reached it's last destination.
        """
        return False if self.schedule else True

    def get_pos(self):
        """
        Parameters:
            None
        Returns:
            Current position of the train.
        """
        if self.rail:
            ratio = self.distance / self.rail.get_length()

            start_x, start_y = self.rail.get_begin()
            end_x, end_y = self.rail.get_end()

            pos_x = int(start_x + ratio * (end_x - start_x))
            pos_y = int(start_y + ratio * (end_y - start_y))

            return pos_x, pos_y

        else:
            return (-100, -100)
