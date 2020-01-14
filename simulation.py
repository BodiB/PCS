import cv2
import numpy as np

from train import Train
from railway import Railway
from station import Station

from config import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, SECONDS_PER_TICK

class Simulation:

    def __init__(self): 
        self.stations = [
            Station(5704, "Zandvoort aan zee"),
            Station(2391, "Overveen"),
            Station(42040, "Haarlem"),
            Station(3090, "Haarlem Spaarnwoude"),
            Station(2730, "Halfweg-Zwanenburg"),
            Station(58008, "Amsterdam Sloterdijk"),
            Station(192178, "Amsterdam Centraal"),
        ]

        # create white background
        self.background = np.zeros((SCREEN_WIDTH, SCREEN_HEIGHT,3), np.uint8) + BACKGROUND_COLOR

        self.ix = -1
        self.iy = -1

        self.tick = 0

    def handle_mouse(self, event,x,y,flags,param):
        if event == cv2.EVENT_MOUSEMOVE:
            self.ix, self.iy = x, y

    def clear_background(self):
        self.background *= 0
        self.background += BACKGROUND_COLOR

    def draw_stations(self):
        
        station_interval = (SCREEN_WIDTH - 150) // (len(self.stations))

        w = 30
        h = 30

        y = SCREEN_HEIGHT // 2 - h // 2
        i = 0
        for s in self.stations:
            x = 150 + i * station_interval
            cv2.rectangle(self.background, (x, y), (x + w, y + h), (0,0,255), -1)

            if self.ix <= x + w and self.ix >= x and self.iy <= y+h and self.iy >= y:
                cv2.putText(self.background, f"{s.get_people()}", (600, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1, cv2.LINE_AA)
                cv2.putText(self.background, f"{s._name}", (600, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1, cv2.LINE_AA)
            i += 1

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
        cv2.putText(self.background, timestring, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)
    
    def start(self):

        # setup simulation window
        cv2.namedWindow('Simulation')
        cv2.setMouseCallback('Simulation', self.handle_mouse)

        # start simulation loop
        while(1):
            self.simulate_steps()
            self.draw_time()
            self.draw_stations()
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
