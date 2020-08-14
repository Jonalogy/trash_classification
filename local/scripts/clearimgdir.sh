#!bin/bash

cd ..
rm -rf images
mkdir images
cd images
mkdir glass metal paper plastic other

for folder in */; do
	cd $folder
	touch .counter.txt
	echo 0 > .counter.txt
	cd ..

done

cd ../scripts

