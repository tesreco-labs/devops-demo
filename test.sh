#!/bin/bash
echo "Starting Build"
python -m unittest
if [ $? -eq 0 ]; then
    echo "Build Success"
else
    echo "Build Failed"
fi