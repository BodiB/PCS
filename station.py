"""
Class to define the station
"""

from simulationEntity import SimulationEntity
from train import Train


class Station(SimulationEntity):

    def __init__(self, daily_capacity: int, name: str, x_coord=0, y_coord=0):
        """
        Parameters:
        -   daily_capacity: number of persons that arrive at the station per day
        -   name: Name of the train station used for display
        -   x_coord: x coordinate of the station used for display
        -   y_coord: y coordinate of the station used for display
        """
        super().__init__()

        self.x, self.y = x_coord, y_coord
        seconds_per_day = 24 * 60 * 60
        ticks_per_day = seconds_per_day // self._interval 

        # chance of a person spwaning per simulation tick
        self._spawn_rate = daily_capacity / ticks_per_day
        self._name = name
        self._people = 0

        self._people_per_spawn = 1 if daily_capacity // ticks_per_day == 0 else daily_capacity // ticks_per_day

        # list to hold all usable rails of the station
        self.rails = []

        # list to hold all present trains at the station
        self.trains = []

        self.spawned = []

        self.spawn_train = False

        if self._name == "Zandvoort aan zee":
            self.spawn_train = True
    
    def simulate(self):
        if self.get_random() <= self._spawn_rate:
             self._people += self._people_per_spawn

        for t in self.spawned:
            t.simulate()

    def get_people(self) -> int:
        """
        Returns the amount of people present at the station
        """
        return self._people

    def get_coord(self):
        """
        Coordinates for drawing
        """
        return (self.x, self.y)

    def attach_rail(self, rail):
        """
        Attach a rail to this station
        """

        self.rails.append(rail)

        if self.spawn_train:
            self.spawned.append(Train(None))
            self.spawned[0].attach_rail(rail)
            self.spawn_train = False

    def add_traject(self, traject):
        pass

    def attach_train(self, train):
        """
        Add train to this station
        """
        self.trains.append(train)
