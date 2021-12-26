#!/usr/bin/python3

#Eng-And 2021-12-08

import sys

def main():
    with open(sys.argv[1], "r") as file:
        info = []
        for f in file:
            info.append([i.split(" ") for i in f.split(" | ")])

        for i in range(len(info)):
            for j in range(len(info[i])):
                info[i][j] = [z.strip() for z in info[i][j]]

        total = 0
        for i in info:
            for j in i[1]:
                if len(j) in [2, 3, 4, 7]:
                    total += 1
        print(total)
            
if __name__ == "__main__":
    main()
