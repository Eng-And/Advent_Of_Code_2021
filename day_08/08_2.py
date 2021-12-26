#!/usr/bin/python3

#Eng-And 2021-12-26

import sys

def main():
    with open(sys.argv[1], "r") as file:
        info = []
        for f in file:
            info.append([i.split(" ") for i in f.split(" | ")])

        for i in range(len(info)):
            for j in range(len(info[i])):
                info[i][j] = [set(z.strip()) for z in info[i][j]]

    total = 0
    
    for i in info:
        unique_numbers = dict()
        tests = [("1",2), ("4",4), ("7",3), ("8",7)]

        for j in i[0]:
            for t in tests:
                if len(j) == t[1]:
                    unique_numbers[t[0]] = j

        num = ""
        for j in i[1]:
            if len(j) == 6:
                if len(j & unique_numbers["4"]) == 4:
                    num += "9"
                elif len(j & unique_numbers["1"]) == 2:
                    num += "0"
                else:
                    num += "6"
            elif len(j) == 5:
                if len(j & unique_numbers["1"]) == 2:
                    num += "3"
                elif len(j & unique_numbers["4"]) == 2:
                    num += "2"
                else:
                    num += "5"
            else:
                for un in unique_numbers.keys():
                    if unique_numbers[un] == j:
                        num += un
        print(num)
        total += int(num)
    print(total)
            
if __name__ == "__main__":
    main()
