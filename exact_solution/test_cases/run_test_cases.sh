#!/bin/bash

# Sample shell script for running test cases that includes
# color coding some output.  Code modeled after code
# from Martin Nester

RED="\033[0;31m"
GREEN="\033[0;32m"
BOLD="\033[1m"
NC="\033[0m" # No Color
BLUE="\033[0;34m"
UL="\e[430m"

echo -e "${BOLD}Test cases:"
echo -e "\t${BOLD}test\tresult\truntime${NC}"

## 

PROG_TO_TEST=../cs412_longestpath_exact.py

for test in test*
do
    cd $test

    start=`python3 -c 'import time; print(time.time())'`
    python3 ../${PROG_TO_TEST} < testInput.txt > testOutput.txt
    end=`python3 -c 'import time; print(time.time())'`
    runtime=$(powershell -Command "[math]::round(($end - $start), 3)")
    # compare the 2nd lines of each file

    # the next 4 lines show a step by step way
    # of getting the first 2 lines of 2 files and storing
    # then in environment variables

    #EXPECTED_2NDLINE=head -n 2 testExpected.txt
    #OUTPUT_2NDLINE=head -n 2 testOutput.txt
    #echo expected ${EXPECTED_2NDLINE}
    #echo output ${OUTPUT_2NDLINE}
  
    # This does the same as the commands above just in a single line

    if [ "$(head -n 2 testExpected.txt)" = "$(head -n 2 testOutput.txt)" ]
    then
        echo -e "\t${test}\t${GREEN}passed\t${BLUE}${runtime}s${NC}"
    else
        echo -e "\t${test}\t${RED}failed\t${BLUE}${runtime}s${NC}"
    fi

    cd ../
done
