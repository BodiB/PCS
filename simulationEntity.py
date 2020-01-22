"""
Class superclass to all simulation components
"""

from config import SECONDS_PER_TICK
import random

class SimulationEntity:

    def __init__(self):
        self._interval = SECONDS_PER_TICK

    def simulate(self):
        raise NotImplementedError

    def get_random(self) -> float:
        return random.uniform(0, 1)

    def get_seconds(self, ticks) -> float:
        return ticks * self._interval

    def get_seconds_remaining(self, ticks) -> float:
        return ticks * self._interval % 60
        
    def get_minutes(self, ticks) -> int:
        seconds = self.get_seconds(ticks)
        return (seconds // 60) % 60
