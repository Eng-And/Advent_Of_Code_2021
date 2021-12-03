#!/bin/bash

#Eng-And 2021-12-03


mapfile -t nums

gamma=0
epsilon=0

foo=${nums[0]}

for index in $(seq 0 $(( ${#foo} - 1 )) )
do
    ones=0
    (( gamma *= 10 ))
    (( epsilon *= 10 ))
    
    for line in ${nums[@]}
    do
	case "${line:index:1}" in
	    1) (( ones += 1 ));;
	esac

    done

    if [[ $ones -gt $(( ${#nums[@]} / 2 )) ]]
    then
	(( gamma += 1))
    else
	(( epsilon += 1 ))
    fi
    
done
echo "$(( $((2#$gamma)) * $((2#$epsilon)) ))"
