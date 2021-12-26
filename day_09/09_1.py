#!/usr/bin/python3

#Eng-And 2021-12-26

import sys

def main():
    data = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            data.append([int(i) for i in line.strip()])

    total_risk = 0
    
    for y in range(len(data)):
        for x in range(len(data[y])):
            lowest = data[y][x] < min([data[i[1]][i[0]] for i in get_surrounding_coords(data, [x, y])])

            if lowest:
                total_risk += data[y][x] + 1

    print(total_risk)

            

            
def get_surrounding_coords(data, point):
    surroundings = []
    for i in [(1,0),(-1,0),(0,1),(0,-1)]:
        surroundings.append([point[j] + i[j] for j in range(2)])

        if not (0 <= surroundings[-1][0] < len(data[0]) and 0 <= surroundings[-1][1] < len(data)):
            del surroundings[-1]
    
    return(surroundings)

if __name__ == "__main__":
    main()
