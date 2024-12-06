#!/bin/bash

if [ -z "$1" ]; then
    echo "ERROR: Missing day number"
    exit 1
fi

YEAR="2024"
NUM=$(printf "%02d" $1)
DAY="day$NUM"
LANG="python"

if [ ! -e "$DAY" ]; then
    mkdir "$LANG/$DAY"
fi


cp $LANG/template/template.py $LANG/$DAY/$DAY.py

tee $LANG/$DAY/test_run.py << EOF
from .$DAY import main

if __name__ == "__main__":
    main("test.txt")
EOF

echo "from .$DAY import *" > $LANG/$DAY/__init__.py
touch $LANG/$DAY/test.txt

curl "https://adventofcode.com/$YEAR/day/$1/input" \
  -H 'referer: https://adventofcode.com/2024/day/2' \
  -o $LANG/$DAY/input.txt
