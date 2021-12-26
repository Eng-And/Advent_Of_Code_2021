#!/usr/bin/python3

#Eng-And 2021-12-26

import sys

def main():
    with open(sys.argv[1], "r") as file:
        data = [line.strip() for line in file]

    point_system = {")" : 3,
                    "]" : 57,
                    "}" : 1197,
                    ">": 25137,
                    }

    close_to_open = {")" : "(",
                     "]" : "[",
                     "}" : "{",
                     ">" : "<",
                     }
    
    
    error_score = 0
    
    for line in data:
        possible_chars = ["(", "[", "{", "<", ")", "]", "}", ">"]

        opened_chunks = []
                
        for char in line:
            if char in close_to_open.values():
                opened_chunks.append(char)
            elif close_to_open[char] == opened_chunks[-1]:
                del opened_chunks[-1]
            else:
                error_score += point_system[char]
                break
            
    print(error_score)

if __name__ == "__main__":
    main()
