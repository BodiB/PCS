"""
Class to define the station
"""

from simulationEntity import SimulationEntity


class Station(SimulationEntity):

    def __init__(self, daily_capacity: int):
        """
        Parameters:
        -   daily_capacity: number of persons that arrive at the station per day
        """
        seconds_per_day = 24 * 60 * 60
        ticks_per_day = seconds_per_day // self._interval 

        # chance of a person spwaning per simulation tick
        self._spawn_rate = daily_capacity / ticks_per_day
