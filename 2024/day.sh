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
  -H 'cookie: _ga=GA1.2.1906575322.1732997985; _gid=GA1.2.582259701.1732997985; session=53616c7465645f5fb1d69a480a4b793faa38dabb2cf744cf7dc3a5cb43b7295ad2b9cb071035e12e7e2f6aa2281a57f13c1aa204c596da4a4eebf9261b6b9c76; _gat=1; _ga_MHSNPJKWC7=GS1.2.1733167273.5.1.1733168945.0.0.0' \
  -H 'referer: https://adventofcode.com/2024/day/2' \
  -o $LANG/$DAY/input.txt