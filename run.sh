#!/bin/bash
# H1bTools can run simply by the following commands.

# CERTIFIED (Default)

python ./src/H1bTools.v3.py -I ../H1b-counting-tool-H1bTool--master/insight_testsuite/tests/test_1/input/h1b_input.csv -out1 ../H1b-counting-tool-H1bTool--master/insight_testsuite/tests/test_1//output/top_10_occupations.txt -out2 ../H1b-counting-tool-H1bTool--master/insight_testsuite/tests/test_1/output/top_10_states.txt


# CERTIFIED-WITHDRAWN, WITHDRAWN or DENIED
#python ./src/H1bTools.v3.py -I /input/h1b_input.csv -out1 /output/top_10_occupations.txt -out2 /output/top_10_states.txt -Cstatus CERTIFIED-WITHDRAWN OR WITHDRAWN OR DENIED 
