"""
Class to describe a traject, with begin and end station and spawn times for the train on the begin station
"""
from simulationEntity import SimulationEntity
from train import Train


class TimeSlot:

    def __init__(self, station, arrival, departure, skip=False):
        """
        A class to represent the arrival and departure times for a station in a given schedule.

        Parameters:
        -   station: the station for which these times are valid
        -   arrival: time to arrive at this station in minutes past the hour
        -   departure: time to leave the station again in minutes past the hour
        -   skip: marks wether the station should be skipped in its given schedule,
                  used for intercities that have to pass the station but don't stop at it.
        """

        self.station = station
        self.arrival = arrival
        self.departure = departure
        self.skip = skip


class Traject(SimulationEntity):

    def __init__(self, times_table: list):
        """
        Parameters:
            - times_table: ordered list of TimeSlots
        """

        super().__init__()

        self.times = times_table

        # contains all trains currently running on this traject
        self.trains = []

        self.on_time = 0
        self.delayed = 0

    def __str__(self):
        string = ""
        for time in self.times:
            string += f"{time.station._name}: arrival at {time.arrival}, departure at {time.departure}\n"

        return string

    def add_timeslot(self, timeslot):
        """
        Adds a timeslot to the current schedule, appends it to the back of the list

        Parameters:
            - timeslot: the timeslot entity to add to this schedule
        """
        self.times.append(timeslot)

    def add_train(self, train):
        """
        Adds a train to this schedulde's memory, in order to keep track of it.

        Parameters:
            - train: the train entity to keep track of
        """
        train.add_schedule(self.times)
        self.trains.append(train)

    def simulate(self, tick):
        """
        This function will simulate the schedules for the given tick. It will make sure that the correct train is spawned at the correct station
        at exactly the time it should depart. It will also add itself to that train, so the train knows which stations to visit.

        Parameters:
            - tick: the current simulation tick, used for timing
        """
        if self.get_minutes(tick) == self.times[0].departure and self.get_seconds_remaining(tick) < self._interval:
            t = Train()
            t.add_schedule(self.times, tick)
            self.trains.append(t)
            self.times[0].station.add_train(t)

        for t in self.trains:
            t.simulate(tick)

            if t.is_terminated():
                self.on_time += t.on_time
                self.delayed += t.delayed

                t.on_time = 0
                t.delayed = 0
