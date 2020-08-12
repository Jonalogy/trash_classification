#!bin/bash

cur=0

cd ../images

for folder in */; do
	cd $folder
	stip=$(echo $folder | cut -d'/' -f 1)
	for file in *.jpg; do
		i=$((i+1))
		@mv $file $stip$cur.jpg 2>/dev/null
	done	
	echo $cur > counter.txt
	cd ..
done

cd ../scripts
