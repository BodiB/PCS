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

        Returns:
            None
        """
        super().__init__()

        self.x, self.y = int(
            x_coord / 1024 * SCREEN_WIDTH), int(y_coord / 1024 * SCREEN_HEIGHT)
        seconds_per_day = 24 * 60 * 60
        ticks_per_day = seconds_per_day // self._interval

        # chance of a person spwaning per simulation tick
        self._name = name

        # list to hold all usable rails of the station
        self.rails = {}

        # list to hold all present trains at the station
        self.trains = []

        # Counters that holds the number of (delayed) trains that passed the station
        self.trains_passed = 0
        self.trains_delayed = 0

        self.trajects = []
        # keep a list of times at which to spawn trains
        self.spawn_times = []

        self.delay = 0

    def simulate(self, ticks):
        """
        Parameter(s):
            - ticks: Current timestamp in ticks.
        Returns:
            None

        Simulates a station by assigning trains to tracks
        """
        trainlist = []
        for t in self.trains:
            target = t.get_target()
            if target:
                if ((ticks >= t.get_departure_tick() + self.get_delay()) or t.get_skip()):
                    t.attach_rail(self.rails[target.station._name], ticks)
                    if not t.get_skip():
                        self.trains_passed += 1
                        t.delay = max(0, self.get_minutes(
                            ticks - t.get_departure_tick()))
                        if t.delay > 0:
                            self.trains_delayed += 1
                    trainlist.append(t)
            if t.is_terminated():
                trainlist.append(t)
        self.derail_train(trainlist)

    def get_delay(self):
        """
        Parameter(s):
            None
        Returns:
            The delay in ticks
        """
        return self.delay * 60 / self._interval

    def derail_train(self, trainlist):
        """
        Parameter(s):
            trainlist: List of trains that have fullfilled their duties.
        Returns:
            None

        Removes trains from tracks
        """
        for train in trainlist:
            self.trains.remove(train)

    def get_coord(self):
        """
        Parameter(s):
            None
        Returns:
            Tuple (X,Y) coordinates of the station.

        Coordinates for drawing
        """
        return (self.x, self.y)

    def attach_rail(self, rail):
        """
        Parameter(s):
            rail: rail entity
        Returns:
            None

        Attach a rail to this station
        """
        self.rails[rail.end_station._name] = rail

    def add_traject(self, traject):
        """
        Parameter(s):
            traject: traject entity
        Returns:
            None

        Adds a traject to this station.
        """
        self.trajects.append(traject)

    def add_train(self, train):
        """
        Parameter(s):
            train: train entity
        Returns:
            None

        Add train to this station
        """
        self.trains.append(train)
