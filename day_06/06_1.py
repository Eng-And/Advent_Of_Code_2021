#!/usr/bin/python3

#Eng-And 2021-12-06

import sys

def main(): #First input file, second amount of days
    with open(sys.argv[1], "r") as file:
        data = [int(i) for i in file.readline().split(",")]

    days = int(sys.argv[2])
    for d in range(days):
        starting_length = len(data)
        for i in range(starting_length):
            if data[i] == 0:
                data[i] = 6
                data.append(8)
            else:
                data[i] -= 1

    print(len(data))

if __name__ == "__main__":
    main()
