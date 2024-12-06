#!/bin/bash

EXACT_SCRIPT_DIR="../exact_solution/cs412_longestpath_exact.py"
APPROX_SCRIPT_DIR="./cs412_longestpath_approx.py"
TEST_CASES_DIR="./test_cases"
OUTPUT_FILE="./approx_runtime_results.txt"

> "${OUTPUT_FILE}"

for TEST_CASE in "${TEST_CASES_DIR}"/input*.txt
do
    if [ "${TEST_CASE}" == "./test_cases/input_1000_vertices.txt" ]
    then
        continue
    fi

    if [ "${TEST_CASE}" == "./test_cases/input_nonoptimal.txt" ]
    then
        continue
    fi

    echo "Running test case: ${TEST_CASE}" >> "${OUTPUT_FILE}"

    echo "Exact solution:" >> "${OUTPUT_FILE}"

    { time python3 "${EXACT_SCRIPT_DIR}" < "${TEST_CASE}" ; } &>> "${OUTPUT_FILE}"

    echo "" >> "${OUTPUT_FILE}"

    echo "Approximate solution:" >> "${OUTPUT_FILE}"

    { time python3 "${APPROX_SCRIPT_DIR}" < "${TEST_CASE}" ; } &>> "${OUTPUT_FILE}"

    echo "-------------------------" >> "${OUTPUT_FILE}"
done