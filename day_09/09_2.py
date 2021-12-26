#!/usr/bin/python3

#Eng-And 2021-12-26

import sys

def main():
    data = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            data.append([int(i) for i in line.strip()])


    basin_sizes = []
            
    for y in range(len(data)):
        for x in range(len(data[y])):
            lowest = data[y][x] < min([data[i[1]][i[0]] for i in get_surrounding_coords(data, [x, y])])

            if lowest:
                basin_sizes.append(find_basin_size(data, [x, y]))

    basin_sizes.sort()
    output = 1
    for i in range(-3, 0):
        output *= basin_sizes[i]

    print(output)
                
            
def get_surrounding_coords(data, point):
    surroundings = []
    for i in [(1,0),(-1,0),(0,1),(0,-1)]:
        surroundings.append([point[j] + i[j] for j in range(2)])

        if not (0 <= surroundings[-1][0] < len(data[0]) and 0 <= surroundings[-1][1] < len(data)):
            del surroundings[-1]
    
    return(surroundings)

def find_basin_size(data, low_point):
    unchecked_points = [low_point]
    new_points = []
    all_points = []

    while unchecked_points != []:
        for up in unchecked_points:
            for sc in get_surrounding_coords(data, up):
                if sc not in new_points and sc not in all_points and data[sc[1]][sc[0]] < 9:
                    new_points.append(sc)

            if up not in all_points:
                all_points.append(up)
        unchecked_points = new_points.copy()
        new_points = []
    return(len(all_points))
        
if __name__ == "__main__":
    main()
