import csv

import numpy as np

if __name__ == "__main__":
    filenames = ["CS10.csv", "HLM10.csv", "LD10.csv", "SD10.csv"]
    for filename in filenames:
        with open(filename) as fin:
            total = 0
            delays = 0
            for row in csv.reader(fin):
                # print(row)
                if row[0] == "NAME":
                    print(f"{filename}")
                else:
                    # print(int(row[1]))
                    total += int(row[1])
                    delays += int(row[2])
            print(f"Total: {total}")
            print(f"Delays: {delays}")
            print("=================")
