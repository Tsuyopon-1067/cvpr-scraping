#!/bin/bash
htmlName="list.html"

if [ $# -eq 1 ]; then
    if [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
        echo "usage: scraping_extract.sh [html file name] [extract word]"
        exit 0
    fi
fi

if [ $# -ge 1 ]; then
    htmlName=$1
fi

python3 scraping.py > tmp_all.csv

if [ $# -ge 2 ]; then
    python3 extract.py tmp_all.csv "$2" > tmp_extract.csv
    python3 html.py tmp_extract.csv > $htmlName
else
    python3 html.py tmp_all.csv > $htmlName
fi
echo save html as $htmlName
rm -f tmp_all.csv tmp_extract.csv
