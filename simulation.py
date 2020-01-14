import cv2
import numpy as np


from train import Train
from railway import Railway
from station import Station

class Simulation:

    def __init__(self): 
        self.stations = [
            Station(1000),
            Station(3200),
            Station(10000)
        ]

    
    def start(self):
        
