"""
Class to describe a part of the railway
"""

from simulationEntity import SimulationEntity
from station import Station


class Railway(SimulationEntity):
    def __init__(self, length: float, speed: float, begin_station: Station, end_station: Station):
        """
        Parameters:
            - length: the length of the railway in kilometers
            - speed: speed in kph

        Returns:
            None
        """

        super().__init__()

        self.begin_station = begin_station
        self.end_station = end_station

        self.x_start = begin_station.x
        self.y_start = begin_station.y

        self.x_end = end_station.x
        self.y_end = end_station.y

        meters_per_second = speed / 3.6

        # max distance per tick in meters
        self._speed = meters_per_second * self._interval

        # length in meters
        self._length = length * 1000

        self.delay = 0

    def get_begin(self) -> (int, int):
        """
        Parameter(s):
            None
        Returns:
            Begin point for drawing
        """
        return (self.x_start, self.y_start)

    def get_end(self) -> (int, int):
        """
        Parameter(s):
            None
        Returns:
            End point for drawing
        """
        return (self.x_end, self.y_end)

    def set_delay(self, delay):
        """
        Parameter(s):
            - delay: Delay in minutes
        Returns:
            None

        Sets the delay of the track
        """
        self.delay = delay

    def get_speed(self):
        """
        Parameter(s):
            None
        Returns:
            Max speed of this given track.
        """
        return self._speed

    def get_length(self):
        """
        Parameter(s):
            None
        Returns:
            Length of the given track
        """
        return self._length
