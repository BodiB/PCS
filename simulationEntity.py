"""
Class superclass to all simulation components
"""

from config import SECONDS_PER_TICK
import random

class SimulationEntity:

    def __init__(self):
        self._interval = SECONDS_PER_TICK

    def simulate(self):
        """
        Function should be overridden by subclasses
        """
        raise NotImplementedError

    def get_random(self) -> float:
        """
        Helper function to return value between 0 and 1
        """
        return random.uniform(0, 1)

    def get_seconds(self, ticks) -> float:
        """
        Parameters:
            - ticks: given simulation tick
        Returns:
            Current simulated second
        """
        return ticks * self._interval

    def get_seconds_remaining(self, ticks) -> float:
        """
        Parameters:
            - ticks: given simulation tick
        Returns:
            Current simulated second, adjusted for minutes
        """
        return ticks * self._interval % 60
        
    def get_minutes(self, ticks) -> int:
        """
        Parameters:
            - ticks: given simulation tick
        Returns:
            Current simulated minute
        """
        seconds = self.get_seconds(ticks)
        return (seconds // 60) % 60
