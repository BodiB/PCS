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
