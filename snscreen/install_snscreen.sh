#!/bin/bash

snscreen_dir=$HOME/snscreen_files
snscreen_binary_dir=$HOME/bin

if [[ $snscreen_dir != `pwd` ]]; then
	if [[ -d $snscreen_dir ]]; then
		echo "Previous installation of snscreen is detected."
		echo "Do you want to overwrite it with new installation? [y/n]"
		read -s -n 1 ans
		if [[ $ans == 'y' ]]; then
			rm -fr $snscreen_dir
		else
			exit
		fi
	fi
	mkdir -p $snscreen_dir
	cp utils/* $snscreen_dir/.
	cp README_sample $snscreen_dir/.
	cp syntax_of_README.txt $snscreen_dir/.
fi

if [[ ! -d $snscreen_binary_dir ]]; then
	echo "'$snscreen_binary_dir' does not exist, creating it..."
	mkdir -p $snscreen_binary_dir
fi
cp utils/snscreen $snscreen_binary_dir/.

echo "=================="
echo "Congratulations!!! snscreen is ready to be used."
echo "Please make sure that '$snscreen_binary_dir' is in your PATH"
echo "=================="
