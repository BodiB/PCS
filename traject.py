"""
Class to describe a traject, with begin and end station and spawn times for the train on the begin station
"""
from simulationEntity import SimulationEntity

class Traject(SimulationEntity):

    def __init__(self, stations: list):
        """
        Parameters:
        -   stations: ordered list of stations that are part of this traject
        """

        super().__init__()

        self.stations = stations
