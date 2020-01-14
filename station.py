"""
Class to define the station
"""

from simulationEntity import SimulationEntity


class Station(SimulationEntity):

    def __init__(self, daily_capacity: int, name: str):
        """
        Parameters:
        -   daily_capacity: number of persons that arrive at the station per day
        """
        super().__init__()
        seconds_per_day = 24 * 60 * 60
        ticks_per_day = seconds_per_day // self._interval 

        # chance of a person spwaning per simulation tick
        self._spawn_rate = daily_capacity / ticks_per_day
        self._name = name
        self._people = 0

        self._people_per_spawn = 1 if daily_capacity // ticks_per_day == 0 else daily_capacity // ticks_per_day
    
    def simulate(self):
        if self.get_random() <= self._spawn_rate:
             self._people += self._people_per_spawn

    def get_people(self) -> int:
        """
        Returns the amount of people present at the station
        """
        return self._people
