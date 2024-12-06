#!/bin/bash

SCRIPT_DIR="./"
TEST_CASE_DIR="./test_cases/input_nonoptimal.txt"

echo "Running non-optimal case"

python3 "${SCRIPT_DIR}/cs412_longestpath_approx.py" < "${TEST_CASE_DIR}"

echo "-------------------------"
