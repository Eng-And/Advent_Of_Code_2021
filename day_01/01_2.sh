#!/bin/bash

#Eng-And 2021-12-01

prev_sum=-1
cur_sum=-1

attempt=0

nums=(-1 -1 -1)
total=0

while read line;
do
    nums=(${nums[1]} ${nums[2]} $line)
    attempt=$((attempt + 1))

    if [[ $attempt -gt 2 ]]
    then

	cur_sum=0
	
	for i in "${nums[@]}"
	do
	    cur_sum=$((cur_sum + i))
	done
	
	if [[ $prev_sum -ne -1 && $cur_sum -gt $prev_sum ]]
	then
	    total=$((total + 1))
	fi
    fi

    prev_sum=$cur_sum
    
done

echo $total
