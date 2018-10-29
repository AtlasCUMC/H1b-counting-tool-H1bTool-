# H1b-counting-tool-H1bTool-

## Introduction

H1btools is command line computational tool, which can be used for H1b visa related analysis. I developed H1btools in python platform, which can be used for any type of data analysis from the state department of US for H1b related visas.

## Useful database

We used the following data to test H1bTools: 

https://www.foreignlaborcert.doleta.gov/performancedata.cfm

## Download 

clone https://github.com/AtlasCUMC/H1b-counting-tool-H1bTool-.git

OR

wget https://github.com/AtlasCUMC/H1b-counting-tool-H1bTool-/archive/master.zip

## Usage

H1btools can use in both Linux (cluster) and MAC machine. 

    python  H1bTools.v3.py  --help
    ************************************************************************* 
      * H1bTools 
     * Version 3.0.0 
     * (C) Oct 24, 2018- Oct 30, 2018 Nephrology Dept of Medicine 
     * Columbia University Medical Center 

     *************************************************************************
    NOTICE: H1bTools beginning analysis at Mon Oct 29 11:54:51 2018
    usage: H1bTools.v3.py [-h] -I The data file, which contains all the data
                          [-out1 Top 10 occupations] [-out2 Top 10 states]
                          [-N TOP_INT] [-Cstatus_index CSTATUS_INDEX]
                          [-Occ_index OCC_INDEX] [-State_index STATE_INDEX]
                          [-Cstatus CSTATUS]

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
      -Cstatus_index CSTATUS_INDEX, --Cstatus_index CSTATUS_INDEX
                            The certified column in the input file
      -Occ_index OCC_INDEX, --Occ_index OCC_INDEX
                            The occupations column in the input file
      -State_index STATE_INDEX, --State_index STATE_INDEX
                            The state column in the input file
      -Cstatus CSTATUS, --Cstatus CSTATUS
                            The status of the case
                        

# H1bTools Input files

H1bTools require the csv file (comma separated) and there will be _NO COMMA_ between in any line csv file such as if:

COMPUTER, INFORMATION and SYSTEMS MANAGERS

You should be remove the comma from the above line since in current version H1bTools is comma sensitive, you can convert the comma to space, and etc. In H1bTools future version, we will try our best to _overcome this issue_. 


# Example

## H1bTools Default (Certified Visas)

    python H1bTools.v3.py -I h1b_input.csv

After running the above command, you will get the following files in the same directory, which contain top 10 occupations and states respectively:


Top 10 occupations: top_10_occupations.txt 

Top 10 States: top_10_states.txt


However, the code can be also used if you do you like top 20 or 30 or any, you can use the extra flag _-N_ in H1bTools:


    python H1bTools.v3.py  –I h1b_input.csv  -N 1 (for example top 1) OR 5 (for example top 5) 50 (for example top 50)_ etc


We used the default columns for CASE_STATUS, SOC_CODE and WORKSITE_STATE in the input file such as CASE_STATUS on column 2, SOC_CODE 24 and WORKSITE_STATE 50 in the input file, however if it is different than that, we can specify them in command line them by using the following command:

    python H1bTools.v3.py -I h1b_input.csv -N 1 (for example top 1) OR 5 (for example top 5) 50 (for example top 50) etc -Cstatus_index (CASE_STATUS) 2 (column 2) OR 3 (column 3) etc -SOC_CODE 24 (column 24) OR etc -WORKSITE_STATE 50 (column 50) OR ETC

## H1bTools for other cases (such as CERTIFIED-WITHDRAWN, DENIED and WITHDRAWN)

H1bTools can be also used to see summary of the CERTIFIED-WITHDRAWN, DENIED and WITHDRAWN if interested by using the following command with extra flag:

     python  H1bTools.v6.py  -I h1b_input.csv -Cstatus CERTIFIED-WITHDRAWN OR DENIED OR WITHDRAWN
 
 It will provide the summary of the CERTIFIED-WITHDRAWN OR DENIED OR WITHDRAWN if user interested.

# Author

Atlas Khan, Department of Medicine (Division Nephrology), Columbia University Medical Centre, New York, USA.

Email: ak4046@cumc.columbia.edu and atlas.akhan@gmail.com

