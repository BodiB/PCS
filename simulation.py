import cv2
import numpy as np

from train import Train
from railway import Railway
from station import Station

from config import *

class Simulation:

    def __init__(self): 
        self.stations = [
            Station(5704, "Zandvoort aan zee", int(160 / 1024 * SCREEN_WIDTH), int(805 / 1024 * SCREEN_HEIGHT)),
            Station(2391, "Overveen", int(210 / 1024 * SCREEN_WIDTH), int(805 / 1024 * SCREEN_HEIGHT)),
            Station(42040, "Haarlem", int(255 / 1024 * SCREEN_WIDTH), int(805 / 1024 * SCREEN_HEIGHT)),
            Station(3090, "Haarlem Spaarnwoude", int(300 / 1024 * SCREEN_WIDTH), int(805 / 1024 * SCREEN_HEIGHT)),
            Station(2730, "Halfweg-Zwanenburg", int(360 / 1024 * SCREEN_WIDTH), int(805 / 1024 * SCREEN_HEIGHT)),
            Station(58008, "Amsterdam Sloterdijk", int(420 / 1024 * SCREEN_WIDTH), int(805 / 1024 * SCREEN_HEIGHT)),
            Station(192178, "Amsterdam Centraal", int(485 / 1024 * SCREEN_WIDTH), int(805 / 1024 * SCREEN_HEIGHT)),
        ]

        self._create_station_hash()

        # attach rails to station
        self._get_station("Zandvoort aan zee").attach_rail(Railway(5.76, 100, self._get_station("Zandvoort aan zee"), self._get_station("Overveen")))
        self._get_station("Overveen").attach_rail(Railway(2, 100, self._get_station("Overveen"), self._get_station("Haarlem")))

        # create white background
        background_image = cv2.imread("background.png")
        self.background_image = cv2.resize(background_image, (SCREEN_WIDTH, SCREEN_WIDTH)) 
        self.background = np.copy(self.background_image)

        self.ix = -1
        self.iy = -1

        self.click_x = -1
        self.click_y = -1

        self.tick = 0

    def _create_station_hash(self):
        """
        Create hashtable to easily access stations
        """
        self.station_hash = {}

        for s in self.stations:
            self.station_hash[s._name] = s

    def _get_station(self, name):
        return self.station_hash[name]

    def handle_mouse(self, event,x,y,flags,param):
        if event == cv2.EVENT_MOUSEMOVE:
            self.ix, self.iy = x, y
    
        if event == cv2.EVENT_LBUTTONDOWN:
            self.click_x, self.click_y = x, y

    def clear_background(self):
        self.background = np.copy(self.background_image)

    def _draw_stations(self):
        w = 15
        h = 15

        for s in self.stations:
            x = s.x - w // 2
            y = s.y - h // 2
            cv2.rectangle(self.background, (x , y), (x + w, y + h), (0,0,255), -1)

            if self.ix <= x + w and self.ix >= x and self.iy <= y+h and self.iy >= y:
                cv2.putText(self.background, f"{s.get_people()}", (20, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(self.background, f"{s._name}", (20, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1, cv2.LINE_AA)

    def _draw_rails(self):
        """
        Draws all rails
        """
        for s in self.stations:
            for r in s.rails:
                cv2.line(self.background, r.get_begin(), r.get_end(), RAIL_COLOR, thickness=RAIL_THICKNESS)
    
    def _draw_trains(self):
        w = 15
        h = 8
        for s in self.stations:
            for t in s.spawned:
                x, y = t.get_pos()
                cv2.rectangle(self.background, (x , y), (x + w, y + h), (255, 0, 0), -1)

    def simulate_steps(self):
        for s in self.stations:
            s.simulate()

        self.tick += 1

    def _get_time(self):
        """
        Returns the simulation time in seconds
        """
        return self.tick * SECONDS_PER_TICK

    def draw_time(self):
        seconds = self._get_time()

        day = seconds // (24 * 60 * 60)
        hour = seconds // (60 * 60)
        minute = (seconds // 60) % 60

        timestring = f"day: {day} {hour}:{minute}"
        cv2.putText(self.background, timestring, (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
    
    def start(self):

        # setup simulation window
        cv2.namedWindow('Simulation')
        cv2.setMouseCallback('Simulation', self.handle_mouse)

        # start simulation loop
        while(1):
            self.simulate_steps()
            self.draw_time()
            self._draw_rails()
            self._draw_stations()
            self._draw_trains()
            cv2.imshow('Simulation', self.background)

            # clear background
            self.clear_background()

            # aquire user input
            k = cv2.waitKey(20) & 0xFF
            if k == 27:
                break
            elif k == ord('a'):
                print (self.ix, self.iy)

        # destory window when simulation ends
        cv2.destroyAllWindows()


if __name__ == "__main__":
    sim = Simulation()
    sim.start()
