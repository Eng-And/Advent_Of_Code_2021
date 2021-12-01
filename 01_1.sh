#!/bin/bash

#Eng-And 2021-12-01

prev=-1
cur=-1

total=0

while read line;
do
    prev=$cur
    cur=$line
    
    if (($cur > $prev && $prev > -1))
    then
	total=$((total + 1))
    fi
    
done

echo $total
