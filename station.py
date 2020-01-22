"""
Class to define the station
"""

from config import SCREEN_HEIGHT, SCREEN_WIDTH
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

        self.x, self.y = int(
            x_coord / 1024 * SCREEN_WIDTH), int(y_coord / 1024 * SCREEN_HEIGHT)
        seconds_per_day = 24 * 60 * 60
        ticks_per_day = seconds_per_day // self._interval

        # chance of a person spwaning per simulation tick
        self._spawn_rate = daily_capacity / ticks_per_day
        self._name = name
        self._people = 0

        self._people_per_spawn = 1 if daily_capacity // ticks_per_day == 0 else daily_capacity // ticks_per_day

        # list to hold all usable rails of the station
        self.rails = {}

        # list to hold all present trains at the station
        self.trains = []

        self.trajects = []
        # keep a list of times at which to spawn trains
        self.spawn_times = []

        self.delay = 0

    def simulate(self, ticks):
        if self.get_random() <= self._spawn_rate:
            self._people += self._people_per_spawn

        minute = self.get_minutes(ticks)
        trainlist = []
        for t in self.trains:
            target = t.get_target()
            if target:
                if ((minute == (t.get_departure() + self.delay) % 60) or t.get_skip()):
                    # print(f"Dispatching train from {self._name} to {target.station._name}")
                    t.attach_rail(self.rails[target.station._name], ticks)
                    trainlist.append(t)
            if t.is_terminated():
                trainlist.append(t)
        self.derail_train(trainlist)

    def get_people(self) -> int:
        """
        Returns the amount of people present at the station
        """
        return self._people

    def derail_train(self, trainlist):
        for train in trainlist:
            self.trains.remove(train)

    def is_free(self):
        return len(self.trains) < 1

    def get_coord(self):
        """
        Coordinates for drawing
        """
        return (self.x, self.y)

    def attach_rail(self, rail):
        """
        Attach a rail to this station
        """
        # print(f"attaching rail at {self._name} to {rail.end_station._name}")
        self.rails[rail.end_station._name] = rail

    def add_traject(self, traject):
        self.trajects.append(traject)

    def add_train(self, train):
        """
        Add train to this station
        """
        # print(f"adding train at {self._name}")
        self.trains.append(train)
