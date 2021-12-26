#!/usr/bin/python3

#Eng-And 2021-12-26

import sys

def main():
    with open(sys.argv[1], "r") as file:
        data = [line.strip() for line in file]

    point_system = {"(" : 1,
                    "[" : 2,
                    "{" : 3,
                    "<" : 4,
                    }

    close_to_open = {")" : "(",
                     "]" : "[",
                     "}" : "{",
                     ">" : "<",
                     }
    
    
    scores = []
    
    for line in data:
        possible_chars = ["(", "[", "{", "<", ")", "]", "}", ">"]

        opened_chunks = []
        cur_score = 0

        corrupted = False
        
        for char in line:
            if char in close_to_open.values():
                opened_chunks.append(char)
            elif close_to_open[char] == opened_chunks[-1]:
                del opened_chunks[-1]
            else:
                corrupted = True
                break

        if not corrupted:
            for char in opened_chunks[::-1]:
                cur_score = cur_score * 5 + point_system[char]

            scores.append(cur_score)

        
    scores.sort()
    print(scores[len(scores) // 2])

if __name__ == "__main__":
    main()
