"""
Class to describe a train on the network
"""

from simulationEntity import SimulationEntity

class Train(SimulationEntity):

    def __init__(self, load_capacity: int, load_rate: int):
        """
        Parameters:
        -   load_capacity: total amount of people that fit in the train
        -   load_rate: number of people per timestep that can enter or leave the train
        """
        self._max_capacity = load_capacity
        self._load_rate = load_rate
        self._current_load = 0

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

        





