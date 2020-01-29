import csv

import numpy as np
            
import matplotlib.pyplot as plt

if __name__ == "__main__":
    filenames = ["CS10.csv", "HLM10.csv", "LD10.csv", "SD10.csv"]
    stations = ["Amsterdam Centraal", "Haarlem", "Leiden Centraal", "Amsterdam Sloterdijk"]
    arrived = []
    delayed = []
    local_deps = []
    for (i,filename) in enumerate(filenames):
        with open(filename) as fin:
            total = 0
            delays = 0
            for row in csv.reader(fin):
                if row[0] == stations[i]:
                    local_deps.append(int(row[1]))
                if row[0] != "NAME":
                    total += int(row[1])
                    delays += int(row[2])
                    
            arrived.append(total)
            delayed.append(delays)

          
    bar_width = 0.25    
    r1 = np.arange(len(arrived))
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]

    Y=['Arrived','Delayed', 'Local departures']
 

    plt.bar(r1, arrived,bar_width, color='#ffcd32',edgecolor='black')
    plt.bar(r2, delayed,bar_width, color='#0062d3',edgecolor='black')
    plt.bar(r3, local_deps,bar_width, color='#212b5c',edgecolor='black')
    plt.xticks([r+ bar_width for r in range(len(stations))], stations, rotation = 40, ha = 'right')

    plt.xlabel('Stations', fontsize=12)
    plt.ylabel('Number of trains', fontsize=12)
    
  
    plt.legend(Y)
    plt.show()
