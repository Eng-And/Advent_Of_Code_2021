#!/usr/bin/python3

#Eng-And 2021-12-04

import sys, re

def main():
    with open(sys.argv[1], "r") as file:
        text = [f.replace("\n", "").strip() for f in file]
    nums = [int(i) for i in text[0].split(",")]


    boards = []
    for line in text[1:]:
        if line == "":
            boards.append([])
        else:
            boards[-1].append([int(i) for i in re.split(" ? ", line)])

    winning_board = None
    index = -1
    winning_list = ["w"] * len(boards[0])

    while winning_board == None and index < len(nums):
        winners = set()
        index += 1
        cur_num = nums[index]
        for b in range(len(boards)):
            for r in range(len(boards[b])):
                boards[b][r] = [i if cur_num != i else "w" for i in boards[b][r]]
  
            for i in range(len(boards[b])):
                if boards[b][i] == winning_list or [r[i] for r in boards[b]] == winning_list:
                    if len(boards) == 1:
                        winning_board = boards[b]
                    else:
                        winners.add(b)

        winner_list = list(winners)
        winner_list.sort()
        for b in winner_list[::-1]:
            del boards[b]
            
    leftovers = 0
    
    for r in boards[0]:
        for c in r:
            if c != "w":
                leftovers += c
    print(leftovers * nums[index])
 
    
if __name__ == "__main__":
    main()
