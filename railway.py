"""
Class to describe a part of the railway
"""

from simulationEntity import SimulationEntity

class Railway(SimulationEntity):
    def __init__(self, length: float, speed: float): 
            """
            Parameters:
            -   length: the length of the railway in kilometers
            -   speed: distance in meters that can be traveled per time unit on this railway

            """

            self._length = length
            self._speed = speed
