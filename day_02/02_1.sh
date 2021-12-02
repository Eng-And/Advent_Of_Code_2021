#!/bin/bash

#Eng-And 2021-12-02

depth=0
horizontal=0

while read line
do
    direction=${line:0:1}
    amount=${line##* }
    case "$direction" in
	f) (( horizontal += amount ));;
	u) (( depth -= amount ));;
	d) (( depth += amount ));;
    esac
    
done

echo $(( horizontal * depth ))
