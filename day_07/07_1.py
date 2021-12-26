#!/usr/bin/python3

#Eng-And 2021-12-07

import sys

def main():
    with open(sys.argv[1], "r") as file:
        positions = [int(i) for i in file.readline().split(",")]

    for i in range(len(positions) + 1):
        cur_sum = 0
        for p in positions:
            cur_sum += abs(p - i)
        if i == 0:
            total = cur_sum
        else:
            total = min(total, cur_sum)
    print(total)

if __name__ == "__main__":
    main()
