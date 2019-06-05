#!/bin/bash
for file_a in *
do
    file_pre=${file_a#*_}
    file_1=${file_pre%.*}
    from=${file_1%.*}
    to=$((10#$from+10))
    echo "convert $file_a ($from to $to) to ../wav/${file_a%.*}.wav"
    ffmpeg -v quiet -i "$file_a" -ar 22050 -ss "$from" -to "$to"   -y "../wav/${file_a%.*}.wav" 
done
