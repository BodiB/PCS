"""
File that recreates the figure by simulating the given delay at
all stations in the 'stations' list.

Parameters:
    - tickCount: The amount of ticks that the simulation will take.
    - delayMinutes: The simulated delay in minutes at the given station.
    - stations: A list of station names on which the delay in delayMinutes
                has to be simulated for tickCount time.
                (approximately 360 ticks per hour)
"""

import csv

import matplotlib.pyplot as plt
import numpy as np

from simulation import Simulation

if __name__ == "__main__":
    # Change this to any positive integer (Tests were done with: 4325)
    tickCount = 4325
    delayMinutes = 10  # Change this to any positive integer
    stations = [
        "Amsterdam Centraal",
        "Haarlem",
        "Leiden Centraal",
        "Amsterdam Sloterdijk"
    ]  # Add any station name here to get more data
    arrived = []
    delayed = []
    local_deps = []

    for delayStation in stations:
        sim = Simulation()
        res = sim.test(tickCount, delayStation, delayMinutes)
        arrived.append(res[0])
        delayed.append(res[1])
        local_deps.append(res[2])

    bar_width = 0.25
    r1 = np.arange(len(arrived))
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]

    Y = ['Arrived', 'Delayed', 'Local departures']

    plt.bar(r1, arrived, bar_width, color='#ffcd32', edgecolor='black')
    plt.bar(r2, delayed, bar_width, color='#0062d3', edgecolor='black')
    plt.bar(r3, local_deps, bar_width, color='#212b5c', edgecolor='black')
    plt.xticks([r + bar_width for r in range(len(stations))],
               stations, rotation=40, ha='right')

    plt.xlabel('Stations', fontsize=12)
    plt.ylabel('Number of trains', fontsize=12)

    plt.legend(Y)
    plt.show()
