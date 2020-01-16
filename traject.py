"""
Class to describe a traject, with begin and end station and spawn times for the train on the begin station
"""
from simulationEntity import SimulationEntity
from train import Train

class TimeSlot:

    def __init__(self, station, arrival, departure):
        """
        Parameters:
        -   station: the station for which these times are valid
        -   arrival: time to arrive at this station in minutes past the hour
        -   departure: time to leave the station again in minutes past the hour
        """

        self.station = station
        self.arrival = arrival
        self.departure = departure

class Traject(SimulationEntity):

    def __init__(self, times_table: list):
        """
        Parameters:
        -   stations: ordered list of TimeSlots
        """

        super().__init__()

        self.times = times_table

        # contains all trains currently running on this traject
        self.trains = []

    def __str__(self):
        string = ""
        for time in self.times:
            string += f"{time.station._name}: arrival at {time.arrival}, departure at {time.departure}\n"
        
        return string

    def add_timeslot(self, timeslot):
        self.times.append(timeslot)

    def add_train(self, train):
        train.add_schedule(self.times)
        self.trains.append(train)

    def simulate(self, tick):
        if self.get_minutes(tick) == self.times[0].departure:
            if self.times[0].station.is_free():
                print(f"Spawning train at {self.times[0].station._name}")
                t = Train()
                t.add_schedule(self.times)
                self.trains.append(t)
                self.times[0].station.add_train(t)
        
        for t in self.trains:
            t.simulate(tick)
            


