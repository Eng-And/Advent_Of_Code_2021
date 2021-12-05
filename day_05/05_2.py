#!/usr/bin/python3

#Eng-And 2021-12-05

import sys

def main():
    #Get File
    with open(sys.argv[1], "r") as file:
        text = [f.replace("\n", "").split(" -> ") for f in file]

    #Replace with lists of tuples of ints for coords
    coords = list()
    for i in range(len(text)):
        coords.append(list())
        coords[-1] = [[int(x) for x in j.split(",")] for j in text[i]]

    #get biggest xy values to make plane
    biggest = [-1,-1]
    for coord in coords:
        for point in coord:
            biggest = [max(biggest[i], point[i]) for i in range(len(biggest))]

    #generate grid
    grid = [([0] * (biggest[0] + 2))] * (biggest[1] + 2) #breaks when only +1
    grid = [i.copy() for i in grid]

    #plot lines
    for coord in coords:

        slope = [(coord[0][1] - coord[1][1]), (coord[0][0] - coord[1][0])] 
        difference_point = [coord[1][i] - coord[0][i] for i in range(len(coord[1]))]
        
        plotted_point = coord[0]
        done = 0 #finished at 2
        while done < 2:
            grid[plotted_point[0]][plotted_point[1]] += 1

            change = [None, None]
            for i in range(len(difference_point)):
                cur_dif = difference_point[i]
                plotted_point[i] += (0) if cur_dif == 0 else (abs(cur_dif) // cur_dif)

            if done == 1 or plotted_point == coord[1]:
                done += 1

    #get number of occurrences
    total = 0
    for r in grid:
        for c in r:
            if c > 1:
                total += 1
    print(total)
    
if __name__ == "__main__":
    main()
