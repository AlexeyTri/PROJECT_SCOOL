#!/bin/bash
#RP=$(realpath $0)
#echo $RP
#dir=$(pwd)
#echo $dir
count=0
for file in /Users/alexeylitovchenko/work_script/BUDGET/*
do
if [ -f "$file" ]
then
count=$[ $count + 1 ]
fi
done
echo $count

if [ $count -eq 4 ]
then
RP=("/Users/alexeylitovchenko/work_script/")
echo $RP
touch $RP/newfile$count.txt
fi
