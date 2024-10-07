#!/usr/bin/bash
YEAR=$1
rm -rf $YEAR
mkdir $YEAR

for i in {01..12}; do
	MONTHSNAME=$(date -d "$YEAR-$i-01" +%b)
	mkdir $YEAR/$MONTHSNAME
	DAYS=$(date -d "$YEAR-$i-01 + 1 month - 1 day" +%d) 
	for j in $(seq -f "%02g" 1 $DAYS); do
		DAYSNAME=$(date -d "$YEAR-$i-$j" +%a)
		echo "$YEAR/$i/$j is a $DAYSNAME" >> $YEAR/$MONTHSNAME/$j.txt
	done
	
done

