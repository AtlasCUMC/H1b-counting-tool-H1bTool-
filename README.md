# H1b-counting-tool-H1bTool-

## Introduction

H1btools is command line computational tool, which can be used for H1b visa related analysis. I devoloped H1btools in python platform, which can be used for any type of data from state department for H1b related visas.

## Useful database

We used for the following data to test H1bTools: 

https://www.foreignlaborcert.doleta.gov/performancedata.cfm

## Usage

H1btools can use in both linux (cluster) and mac machine. 

 python H1bTools.v3.py --help

************************************************************************* 
  * H1bTools 
 * Version 3.0.0 
 * (C) 2018-2018 Nephrology Dept of Medicine 
 * Columbia University Medical Center 

*************************************************************************

NOTICE: H1bTools beginning analysis at Fri Oct 26 10:42:07 2018

usage: H1bTools.v3.py [-h] -I The data file, which contains all the data
                      [-out1 Top 10 occupations] [-out2 Top 10 states]
                      [-N TOP_INT] [-Cer_index CER_INDEX]
                      [-Occ_index OCC_INDEX] [-state_index STATE_INDEX]

The H1bTools is computational tool, which can be use for H1b visa related
analysis:

optional arguments:
  -h, --help            show this help message and exit
  -I The data file, which contains all the data, --Input The data file, which contains all the data
                        The data of H1b application
  -out1 Top 10 occupations, --o1 Top 10 occupations
                        The output file of top 10 occupations
  -out2 Top 10 states, --o2 Top 10 states
                        The output file of top 10 States
  -N TOP_INT, --top_int TOP_INT
                        Percentage of top 10 occupations and States
  -Cer_index CER_INDEX, --Cer_index CER_INDEX
                        The certified column in the input file
  -Occ_index OCC_INDEX, --Occ_index OCC_INDEX
                        The occupations column in the input file
  -state_index STATE_INDEX, --state_index STATE_INDEX
                        The state column in the input file
                        

# H1bTools Input files

H1bTools require the csv file (comma separated file) and there will be _NO COMMA_ between in csv file such as if:

COMPUTER, INFORMATION and SYSTEMS MANAGERS

From the above, should be remove the comma since in current version H1bTools is comman sensittaive, you comma to space, and etct. In our H1bTools future version, we will try our best to overcome this issue. 


# Example

## H1bTools Default (Certified Visas)

python H1bTools.v3.py -I h1b_input.csv

After running the above command, you will get the follwing files in the same directory, which contains top 10 occupations and states:


Top 10 occupations: top_10_occupations.txt 

Top 10 States: top_10_states.txt


However, the code can be also used if you do you like top 20 or 30 or any, you can use the extra flag -N in H1bTools:


python H1bTools.v3.py -I H-1B_Disclosure_Data_FY17.csv -N 1 (for example top 1) OR 5 (for example top 5) 50 (for example top 50) etc


We used default columns for CASE_STATUS, SOC_CODE and WORKSITE_STATE in input file such as CASE_STATUS on column 2, SOC_CODE 24 and WORKSITE_STATE 50, however if it is different than that, we can specifiy in commandline them by using the following command:

python H1bTools.v3.py -I h1b_input.csv -N 1 (for example top 1) OR 5 (for example top 5) 50 (for example top 50) etc Cstatus_index

## H1bTools for other cases (such as CERTIFIED-WITHDRAWN, DENIED and WITHDRAWN)

H1bTools can be also used to see summary of the CERTIFIED-WITHDRAWN, DENIED and WITHDRAWN if interested by using the following command with extrat flag:

 python  H1bTools.v6.py  -I h1b_input.csv -Cstatus CERTIFIED-WITHDRAWN OR DENIED OR WITHDRAWN
 
 It will provide the summay of the CERTIFIED-WITHDRAWN OR DENIED OR WITHDRAWN if interested.

# Author

Atlas Khan, Department of Medicine (Division Nephrology), Columbia University Medical Centre, New York, USA.

Email: ak4046@cumc.columbia.edu and atlas.akhan@gmail.com
