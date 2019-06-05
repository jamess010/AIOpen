#!/bin/sh
for file_a in *
do
    echo "convert $file_a to ../wav/${file_a%.*}.wav"
    ffmpeg -v quiet -i "$file_a" -ar 22050 -y "../wav/${file_a%.*}.wav"
done
