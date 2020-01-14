"""
Class superclass to all simulation components
"""

from config import SECONDS_PER_TICK

class SimulationEntity:

    def __init__(self):
        self._interval = SECONDS_PER_TICK

    def simulate(self):
        raise NotImplementedError
