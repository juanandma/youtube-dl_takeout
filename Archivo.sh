#!/bin/bash


while read -r line
do 
    youtube-dl -o '~/Videos/%(title)s.%(ext)s' "https://www.youtube.com/watch?v=$(echo "$line" | cut -d ',' -f1)"
done < 'Liked videos.csv'
