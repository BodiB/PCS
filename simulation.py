import cv2
import numpy as np

from config import *
from config import (BACKGROUND_COLOR, SCREEN_HEIGHT, SCREEN_HEIGHT_B,
                    SCREEN_WIDTH, SCREEN_WIDTH_B, SECONDS_PER_TICK)
from data.rails import rail_list, rail_list_NL
from data.timesheets import timeslots, timeslots_NL
from railway import Railway
from station import Station
from train import Train
from traject import TimeSlot, Traject


class Simulation:

    def __init__(self, map="NH"):
        if map == "NL":
            from data.stationsNL import stations_list
            timeslots.extend(timeslots_NL)
            rail_list.extend(rail_list_NL)
        else:
            from data.stations import stations_list
        self.stations = stations_list
        self._create_station_hash()

        self.schedules = []

        self.map = map

        self.pause = False

        # create timeslots
        for schedule in timeslots:
            current = []
            last = -1
            hour = False
            firststop = schedule[0]
            laststop = schedule[-1]
            for slot in schedule:
                slot1 = slot[1]
                slot2 = slot[2]
                if len(slot) <= 3:
                    slot3 = False
                else:
                    slot3 = slot[3]
                if slot1 < 0 and slot2 < 0:
                    slot3 = True
                if ((slot1 > slot2 and slot2 >= 0) or (slot1 < last and slot1 >= 0)):
                    hour = True
                if hour:
                    if slot1 >= 0 and (slot1 <= slot2 or slot2 < 0):
                        slot1 += 60
                        if slot1 >= 0:
                            while slot1 < last:
                                slot1 += 60
                                # print(f"+60, slot1 {slot1} op {slot[0]} orig{firststop[0]}@{firststop[2]} dest{laststop[0]}")
                    if slot[2] >= 0:
                        slot2 += 60
                        if slot2 >= 0:
                            while slot2 < slot1:
                                slot2 += 60
                                # print(f"+60, slot2 {slot2} op {slot[0]} orig{firststop[0]}@{firststop[2]} dest{laststop[0]}")
                    current.append(TimeSlot(self._get_station(
                        slot[0]), slot1, slot2, slot3))
                else:
                    current.append(TimeSlot(self._get_station(
                        slot[0]), slot1, slot2, slot3))
                if slot2 >= 0:
                    last = slot2
            self.schedules.append(Traject(current))

        for r in rail_list:
            # if r in connection.keys():
            #     for c in connection[r]:
            #         self._get_station(c[0]).attach_rail(
            #             Railway(c[2], c[3], self._get_station(c[0]), self._get_station(c[1])))
            #         self._get_station(c[1]).attach_rail(
            #             Railway(c[2], c[3], self._get_station(c[1]), self._get_station(c[0])))
            # else:
            self._get_station(r[0]).attach_rail(
                Railway(r[2], r[3], self._get_station(r[0]), self._get_station(r[1])))
            self._get_station(r[1]).attach_rail(
                Railway(r[2], r[3], self._get_station(r[1]), self._get_station(r[0])))

        # create white background
        if map == "NL":
            background_image = cv2.imread("backgroundNL.jpg")
            self.background_image = cv2.resize(
                background_image, (SCREEN_WIDTH_B, SCREEN_HEIGHT_B))
        else:
            background_image = cv2.imread("background.png")
            self.background_image = cv2.resize(
                background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.train_image = cv2.imread("logo.png")
        self.background2 = cv2.imread("logo.png")
        self.background2 = cv2.resize(self.background2, (400, 300))
        self.background_image2 = np.copy(self.background2)
        self.train_image = cv2.resize(self.train_image, (30, 16))

        black = np.all(self.train_image == [0, 0, 0], axis=-1)

        self.train_image[black] = [0, 190, 255]

        self.background = np.copy(self.background_image)

        self.ix = -1
        self.iy = -1

        self.click_x = -1
        self.click_y = -1

        self.clickr_x = -1
        self.clickr_y = -1

        self.tick = 0
        self.selected_train = None

    def _create_station_hash(self):
        """
        Create hashtable to easily access stations
        """
        self.station_hash = {}

        for s in self.stations:
            self.station_hash[s._name] = s

    def _get_station(self, name):
        return self.station_hash[name]

    def handle_mouse(self, event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE:
            self.ix, self.iy = x, y
        if event == cv2.EVENT_LBUTTONDOWN and flags == (cv2.EVENT_FLAG_SHIFTKEY + cv2.EVENT_FLAG_LBUTTON):
            self.clickr_x, self.clickr_y = x, y
        elif event == cv2.EVENT_LBUTTONDOWN:
            train = False
            w = 15
            h = 15
            self.click_x, self.click_y = x, y
            for s in self.stations:
                x = s.x - w // 2
                y = s.y - h // 2
                if self.click_x <= x + w and self.click_x >= x and self.click_y <= y + h and self.click_y >= y:
                    train = True
            w = 30
            h = 16
            for s in self.schedules:
                for t in s.trains:
                    x, y = t.get_pos()
                    if self.click_x <= x + w and self.click_x >= x and self.click_y <= y + h and self.click_y >= y:
                        train = True
            if not train:
                self.selected_train = None

    def clear_background(self):
        self.background = np.copy(self.background_image)
        self.background2 = np.copy(self.background_image2)

    def _draw_stations(self):
        w = 15
        h = 15

        for s in self.stations:
            x = s.x - w // 2
            y = s.y - h // 2
            cv2.rectangle(self.background, (x, y),
                          (x + w, y + h), (0, 0, 255), -1)

            if self.ix <= x + w and self.ix >= x and self.iy <= y + h and self.iy >= y:
                cv2.putText(self.background2, f"Trains: {len(s.trains)}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                cv2.putText(self.background2, f"{s._name}", (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                cv2.putText(self.background2, f"Delay: {s.delay} minutes", (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

            if self.click_x <= x + w and self.click_x >= x and self.click_y <= y + h and self.click_y >= y:
                self.click_x = -1
                self.click_y = -1
                s.delay += 1

            if self.clickr_x <= x + w and self.clickr_x >= x and self.clickr_y <= y + h and self.clickr_y >= y:
                self.clickr_x = -1
                self.clickr_y = -1

                s.delay -= 1
                s.delay = max(s.delay, 0)

    def _draw_rails(self):
        """
        Draws all rails
        """
        for s in self.stations:
            for r in s.rails.values():
                cv2.line(self.background, r.get_begin(), r.get_end(),
                         RAIL_COLOR, thickness=RAIL_THICKNESS)

    def _draw_trains(self):
        w = 30
        h = 16
        for s in self.schedules:
            for t in s.trains:
                x, y = t.get_pos()
                self.background[y:y + h, x:x + w, :] = self.train_image[:, :]
                # cv2.rectangle(self.background, (x, y),
                #               (x + w, y + h), TRAIN_COLOR, -1)
                if self.click_x <= x + w and self.click_x >= x and self.click_y <= y + h and self.click_y >= y:
                    self.selected_train = t
                    self.click_x = -1
                    self.click_y = -1

        if self.selected_train:
            try:
                cv2.putText(self.background2, f"Current target: {self.selected_train.get_next_stop().station._name}", (20, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                cv2.putText(self.background2, f"Current speed: {self.selected_train.get_speed_kph()}", (20, 165), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                cv2.putText(self.background2, self.selected_train.get_data()[
                            0], (20, 180), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
                cv2.putText(self.background2, self.selected_train.get_data()[
                            1], (20, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 1, cv2.LINE_AA)
                # cv2.putText(self.background2, f"Intercity: {self.selected_train.get_skip()}", (20, 180), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
            except:
                pass

    def _draw_stats(self):
        on_time = 0
        delayed = 0

        for s in self.schedules:
            on_time += s.on_time
            delayed += s.delayed

        total = on_time + delayed

        if total != 0:
            on_time_percent = round(on_time / total * 100, 1)
            delayed_percent = round(delayed / total * 100, 1)
        else:
            on_time_percent = 100
            delayed_percent = 0

        cv2.putText(self.background2, f"On time: {on_time_percent} %", (20, 230), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.putText(self.background2, f"Delayed: {delayed_percent} %", (20, 255), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

    def simulate_steps(self):
        for s in self.schedules:
            s.simulate(self.tick)

        for s in self.stations:
            s.simulate(self.tick)

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
        cv2.putText(self.background2, timestring, (20, 25),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    def start(self):

        # setup simulation window
        if self.map == "NL":
            cv2.namedWindow("Simulation", cv2.WND_PROP_FULLSCREEN)
            cv2.namedWindow("Data")
            # cv2.setWindowProperty(
            #     "Simulation", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        else:
            cv2.namedWindow('Simulation')
        cv2.setMouseCallback('Simulation', self.handle_mouse)

        # start simulation loop
        while(1):
            if not self.pause:
                self.simulate_steps()
            self.draw_time()
            self._draw_rails()
            self._draw_stations()
            self._draw_trains()
            self._draw_stats()
            cv2.imshow('Simulation', self.background)
            cv2.imshow('Data', self.background2)

            # clear background
            self.clear_background()

            # aquire user input
            k = cv2.waitKey(20) & 0xFF
            if k == ord('p'):
                self.pause = not self.pause
            if k == 27:
                break
            elif k == ord('a'):
                print (self.ix, self.iy)

        # destory window when simulation ends
        cv2.destroyAllWindows()

    def test(self):
        # setup simulation window
        cv2.namedWindow("Simulation", cv2.WND_PROP_FULLSCREEN)
        cv2.setMouseCallback('Simulation', self.handle_mouse)

        while(1):
            self._draw_stations()
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
    choice = input("""
                   A: North Holland Rail
                   B: Entire dutch rail network operated by NS
                   Please enter your choice: """)
    if choice == "B" or choice == "b":
        sim = Simulation("NL")
    else:
        sim = Simulation()
    sim.start()
    # sim.test()
