#!/usr/bin/python3

#Eng-And 2021-12-06

import sys

def main(): #First input file, second amount of days
    with open(sys.argv[1], "r") as file:
        data = [int(i) for i in file.readline().split(",")]
    fish = [data.count(i) for i in range(9)]
    print(fish)

    days = int(sys.argv[2])
    for d in range(days):
        fish[7] += fish[0]
        fish.append(fish.pop(0))

    total = 0
    for i in fish:
        total += i
    print(total)
    

if __name__ == "__main__":
    main()
