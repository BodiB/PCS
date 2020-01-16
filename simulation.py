import cv2
import numpy as np

from config import (BACKGROUND_COLOR, SCREEN_HEIGHT, SCREEN_WIDTH,
                    SECONDS_PER_TICK)
from railway import Railway
from station import Station
from train import Train

from config import *

class Simulation:

    def __init__(self):
        self.stations = [
            # Station(5704, "Zandvoort aan zee", int(160 / 1024 * SCREEN_WIDTH), int(805 / 1024 * SCREEN_HEIGHT)),
            # Station(2391, "Overveen", int(210 / 1024 * SCREEN_WIDTH), int(805 / 1024 * SCREEN_HEIGHT)),
            # Station(42040, "Haarlem", int(255 / 1024 * SCREEN_WIDTH), int(805 / 1024 * SCREEN_HEIGHT)),
            # Station(3090, "Haarlem Spaarnwoude", int(300 / 1024 * SCREEN_WIDTH), int(805 / 1024 * SCREEN_HEIGHT)),
            # Station(2730, "Halfweg-Zwanenburg", int(360 / 1024 * SCREEN_WIDTH), int(805 / 1024 * SCREEN_HEIGHT)),
            # Station(58008, "Amsterdam Sloterdijk", int(420 / 1024 * SCREEN_WIDTH), int(805 / 1024 * SCREEN_HEIGHT)),
            # Station(192178, "Amsterdam Centraal", int(485 / 1024 * SCREEN_WIDTH), int(805 / 1024 * SCREEN_HEIGHT)),
            Station(5704, "Zandvoort aan zee", 160, 805),
            Station(2391, "Overveen", 210, 805),
            Station(42040, "Haarlem", 254, 805),
            Station(3090, "Haarlem Spaarnwoude", 300, 805),
            Station(2730, "Halfweg-Zwanenburg", 360, 805),
            Station(58008, "Amsterdam Sloterdijk", 422, 805),
            Station(192178, "Amsterdam Centraal", 485, 805),
            # # UITBREIDING VAN BASIS:
            # Station(0, "Den Helder", 258, 80),
            # Station(0, "Den Helder Zuid", 278, 100),
            # Station(0, "Anna Paulowna", 325, 180),
            # Station(0, "Schagen", 325, 278),
            # Station(0, "Bloemendaal", 252, 769),
            # Station(0, "Santpoort Zuid", 252, 744),
            # Station(0, "Santpoort Noord", 252, 719),
            # Station(0, "Driehuis", 252, 700),
            # Station(0, "Beverwijk", 271, 668),
            # Station(0, "Heemskerk", 293, 646),
            # Station(0, "Uitgeest", 287, 599),
            # Station(0, "Castricum", 269, 563),
            # Station(0, "Heiloo", 269, 530),
            # Station(0, "Alkmaar", 271, 490),
            # Station(0, "Alkmaar Noord", 277, 472),
            # Station(0, "Heerhugowaard", 307, 437),
            # Station(0, "Krommenie-Assendelft", 329, 637),
            # Station(0, "Wormerveer", 348, 659),
            # Station(0, "Zaandijk Zaanse Schans", 367, 679),
            # Station(0, "Koog aan de Zaan", 383, 698),
            # Station(0, "Zaandam", 411, 731),
            # Station(0, "Zaandam Kogerveld", 425, 691),
            # Station(0, "Purmerend Weidevenne", 505, 608),
            # Station(0, "Purmerend", 519, 579),
            # Station(0, "Purmerend Overwhere", 519, 555),
            # Station(0, "Hoorn", 519, 416),
            # Station(0, "Hoorn Kersenboogerd", 539, 416),
            # Station(0, "Obdam", 390, 417),
            # Station(0, "Hoogkarspel", 612, 385),
            # Station(0, "Bovenkarspel-Grootebroek", 650, 368),
            # Station(0, "Bovenkarspel Flora", 668, 368),
            # Station(0, "Enkhuizen", 701, 368),
            # Station(0, "Lelystad Centrum", 878, 567),
            # Station(0, "Almere Oostvaarders", 794, 720),
            # Station(0, "Almere Buiten", 771, 734),
            # Station(0, "Almere Parkwijk", 732, 734),
            # Station(0, "Almere Centrum", 710, 758),
            # Station(0, "Almere Muziekwijk", 700, 767),
            # Station(0, "Almere Poort", 670, 798),
            # Station(0, "Weesp", 577, 849),
            # Station(0, "Diemen", 532, 849),
            # Station(0, "Amsterdam Muiderpoort", 485, 840),
            # Station(0, "Amsterdam Amstel", 487, 878),
            # Station(0, "Diemen Zuid", 530, 877),
            # Station(0, "Duivendrecht", 510, 899),
            # Station(0, "Amsterdam Bijlmer Arena", 527, 918),
            # Station(0, "Amsterdam Holendrecht", 541, 935),
            # Station(0, "Abcoude", 557, 945),
            # Station(0, "Amsterdam Zuid", 419, 884),
            # Station(0, "Amsterdam RAI", 443, 884),
            # Station(0, "Schiphol Airport", 305, 899),
            # Station(0, "Hoofddorp", 278, 916),
            # Station(0, "Nieuw Vennep", 251, 945),
            # Station(0, "Voorhout", 173, 982),
            # Station(0, "Hillegom", 173, 899),
            # Station(0, "Heemstede-Aerdenhout", 214, 844),
            # Station(0, "Amsterdam Lelylaan", 397, 841),
        ]

        self._create_station_hash()

        # attach rails to station
        self._get_station("Zandvoort aan zee").attach_rail(Railway(5.76, 100, self._get_station("Zandvoort aan zee"), self._get_station("Overveen")))
        self._get_station("Overveen").attach_rail(Railway(2, 100, self._get_station("Overveen"), self._get_station("Haarlem")))

        # create white background
        background_image = cv2.imread("background.png")
        self.background_image = cv2.resize(
            background_image, (SCREEN_WIDTH, SCREEN_WIDTH))
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
            cv2.rectangle(self.background, (x, y),
                          (x + w, y + h), (0, 0, 255), -1)

            if self.ix <= x + w and self.ix >= x and self.iy <= y + h and self.iy >= y:
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
        # SECONDS IN TIME STRING:
        # second = (seconds) % 60
        # timestring = f"day: {day} {hour}:{minute}:{second}"

        timestring = f"day: {day} {hour}:{minute}"
        cv2.putText(self.background, timestring, (20, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

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

    def test(self):
        # setup simulation window
        cv2.namedWindow('Simulation')
        cv2.setMouseCallback('Simulation', self.handle_mouse)

        while(1):
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


if __name__ == "__main__":
    sim = Simulation()
    sim.start()
    # sim.test()
