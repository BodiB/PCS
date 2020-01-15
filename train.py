"""
Class to describe a train on the network
"""

from simulationEntity import SimulationEntity
from traject import Traject

class Train(SimulationEntity):

    def __init__(self, traject: Traject, load_capacity: int = 0, load_rate: int = 0):
        """
        Parameters:
        -   load_capacity: total amount of people that fit in the train
        -   load_rate: number of people per timestep that can enter or leave the train
        """
        self._max_capacity = load_capacity
        self._load_rate = load_rate
        self._current_load = 0

        self._traject = traject

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

    def attach_rail(self, rail):
        self.distance = 0
        self.rail = rail

    def simulate(self):
        if self.rail:
            self.distance += self.rail.get_speed()
            
            # train arrived at station
            if self.distance >= self.rail.get_length():
                end = self.rail.end_station
                end.attach_train(self)
                self.rail = None

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

        





