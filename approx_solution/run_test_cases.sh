#!/bin/bash

SCRIPT_DIR="./"
TEST_CASE_DIR="./test_cases"

INPUT_FILES=$(ls ${TEST_CASE_DIR}/input*.txt)

for INPUT_FILE in ${INPUT_FILES}
do
    TEST_NAME=$(basename ${INPUT_FILE})
    echo "Running test case ${TEST_NAME}"

    python3 "${SCRIPT_DIR}/cs412_longestpath_approx.py" < "${INPUT_FILE}"

    echo "-------------------------"
done