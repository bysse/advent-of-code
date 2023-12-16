#!/bin/bash

if [ -z "$1" ]; then
    echo "ERROR: Missing day number"
    exit 1
fi

echo "> cp python/template.py python/day$1.py"
cp python/template.py python/day$1.py

echo "> touch input/test$1.txt"
touch input/test$1.txt

echo "> touch input/input$1.txt"
touch input/input$1.txt
