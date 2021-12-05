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

        index += 1
        cur_num = nums[index]
        for board in boards:
            for r in range(len(board)):
                board[r] = [i if cur_num != i else "w" for i in board[r]]
  
            for i in range(len(board)):
                if board[i] == winning_list or [r[i] for r in board] == winning_list:
                    winning_board = board

            
    leftovers = 0
    
    for r in winning_board:
        for c in r:
            if c != "w":
                leftovers += c
    print(leftovers * nums[index])
 
    
if __name__ == "__main__":
    main()
