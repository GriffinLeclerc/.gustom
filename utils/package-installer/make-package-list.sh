#!/bin/bash

sudo apt list --installed > tmp.txt

while read -r line; do 
    # var=$line
    name=${line%/*} # retain chars before the first /
    echo $name >> packages.txt
done < tmp.txt

rm tmp.txt