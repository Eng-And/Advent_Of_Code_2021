#!/bin/bash

#Eng-And 2021-12-03

output=(0 0)
mapfile -t orig_nums
foo=${orig_nums[0]}

for attempt in {0..1}
do
    nums=(${orig_nums[@]})    
    
    for index in $(seq 0 $(( ${#foo} - 1 )) )
    do
	ones=0
	zeros=0

	for line in ${nums[@]}
	do
	    case "${line:index:1}" in
		1) (( ones += 1 ));;
		0) (( zeros += 1));;
	    esac

	done

	if [[ $ones -ge $zeros ]]
	then
	    common_num=1
	else
	    common_num=0
	fi

	bad_num=$(( $((attempt + common_num)) % 2 ))
	
	for i in $(seq 0 ${#nums[@]})
	do
	    line=${nums[i]}
	    case "${line:$index:1}" in
		$bad_num)nums[i]="b";;
	    esac
	done

	total=0
        for n in ${nums[@]}
        do
            if (( n != "b" ))
            then
                (( total += 1 ))
		ans=$n
            fi
        done

	if [[ $total -eq 1 ]]
	then
	    output[$attempt]=$ans
	    break
	fi
	
    done
done

echo "$(( $(( 2#${output[0]} )) * $(( 2#${output[1]} )) )) "
