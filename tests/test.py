import csv

import numpy as np

if __name__ == "__main__":
    with open("SD10.csv") as fin:
        total = 0
        delays = 0
        for row in csv.reader(fin):
            # print(row)
            if row[0] == "NAME":
                print("skip")
            else:
                # print(int(row[1]))
                total += int(row[1])
                delays += int(row[2])
        print(total)
        print(delays)
