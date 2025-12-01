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

if [ ! -e $LANG/$DAY/$DAY.py ]; then
  cp $LANG/template/template.py $LANG/$DAY/$DAY.py
fi

tee $LANG/$DAY/test_run.py << EOF
from .$DAY import main

if __name__ == "__main__":
    main("test.txt")
EOF

tee $LANG/$DAY/__main__.py << EOF
import os
import sys
from .$DAY import main
input_file = os.path.join(os.path.dirname(__file__), "input.txt")

if len(sys.argv) > 1:
    input_file = sys.argv[1]

main(input_file)
EOF


echo "from .$DAY import *" > $LANG/$DAY/__init__.py
touch $LANG/$DAY/test.txt

if [ ! -e $LANG/$DAY/input.txt ]; then
  touch $LANG/$DAY/input.txt
fi