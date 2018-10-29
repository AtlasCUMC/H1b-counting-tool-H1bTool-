from __future__ import division
#!/usr/bin/env python
# H1bTools.v3.py
# C: Oct 24, 2018
# M: Oct 30, 2018
# A: Atlas Khan <atlas.akhan@gmail.com> and <ak4046@cumc.columbia.edu>
# Columbia University Medical Center, New York.
import time
now = time.strftime("%c")
print ("************************************************************************* \n  * H1bTools \n * Version 3.0.0 \n * (C) Oct 24, 2018- Oct 30, 2018 Nephrology Dept of Medicine \n * Columbia University Medical Center \n \n *************************************************************************")
print ("NOTICE: H1bTools beginning analysis at %s"  % now )
start_time = time.time()
import sys, argparse, os
import collections
prog_name = 'H1bTools.v3.py'

def main():
    parser = argparse.ArgumentParser(description='The H1bTools is computational tool, which can be use for H1b visa related analysis:', prog = prog_name)
    parser.add_argument('-I', '--Input',  required = True, metavar = 'The data file, which contains all the data', type = str, help ='The data of H1b application')
    parser.add_argument('-out1', '--o1',  required = False,default='top_10_occupations.txt', metavar = 'Top 10 occupations', type = str, help ='The output file of top 10 occupations')
    parser.add_argument('-out2', '--o2',  required = False,default='top_10_states.txt', metavar = 'Top 10 states', type=str, help ='The output file of top 10 States')
    parser.add_argument('-N', '--top_int',  required = False,default='11', type=int, help ='Percentage of top 10 occupations and States')
    parser.add_argument('-Cstatus_index', '--Cstatus_index',  required = False,default='2', type=int, help ='The certified column in the input file')
    parser.add_argument('-Occ_index', '--Occ_index',  required = False,default='24', type=int, help ='The occupations column in the input file')
    parser.add_argument('-State_index', '--State_index',  required = False,default='50', type=int, help ='The state column in the input file')
    parser.add_argument('-Cstatus', '--Cstatus', required = False,default='CERTIFIED', type=str, help ='The status of the case')
    args = parser.parse_args()

    Input=args.Input
    o1=args.o1
    o2=args.o2
    top_int=args.top_int
    Occ_index=args.Occ_index
    State_index=args.State_index
    Cstatus_index=args.Cstatus_index
    Cstatus=args.Cstatus
    
    try:
        check=open(Input, 'r')
    except IOError:
            print "ERROR: The Input H1b data file is required"
            sys.exit()
    else:
        print "NOTICE: The Input H1b data file is reading"

##############In this block, we need to extract the data columns, we are interested in###################################

    if (Cstatus=="CERTIFIED"):
        print "NOTICE: Doing analysis only for CERTIFIED CASE" 
        dict_lines = {}
    
        output1=open(o1+"_temp",'w')
        output2=open(o2+"_temp",'w')
        p=len(open(Input).readlines())
    
        def certified_filter(Cstatus_index,Cstatus,Occ_index,State_index): ##Cer_index is column of visa status, Occ_index is occputaion status and state_index is column, where the state is given
            file1=open(Input)
            for line1 in file1.readlines():
                line1=line1.strip()
                line2=line1.split(",")
                if line2[Cstatus_index-1]==Cstatus:
                    line4= line2[Occ_index-1] 
                    line5= line2[State_index-1]
                    output1.write('%s\n' % line4)
                    output2.write('%s\n' % line5)
                else:
                    print "NOTICE: There is no CERTIFIED CASE; maybe it is missing OR it is CERTIFIED-WITHDRAWN OR WITHDRAWN OR DENIED"
            output1.close()
            output2.close()
        certified_filter(Cstatus_index,Cstatus,Occ_index,State_index)
    else:
        
        print "NOTICE: Doing analysis only for" +" "+ Cstatus +" "+ "CASE"
    
        output1=open(o1+"_temp",'w')
        output2=open(o2+"_temp",'w')
        p=len(open(Input).readlines())
    
        def certified_filter(Cstatus_index,Cstatus,Occ_index,State_index): ##Cer_index is column of visa status, Occ_index is occputaion status and state_index is column, where the state is given
            file1=open(Input)
            for line1 in file1.readlines():
                line1=line1.strip()
                line2=line1.split(",")

                if line2[Cstatus_index-1]==Cstatus:
                    line4=line2[Occ_index-1]
                    line5=line2[State_index-1]
                    output1.write('%s\n' % line4)
                    output2.write('%s\n' % line5)
                else:
                    print "NOTICE: There is no" +" "+ Cstatus +" "+  "CASE, maybe there is other CASE"
            output1.close()
            output2.close()
        certified_filter(Cstatus_index,Cstatus,Occ_index,State_index)

#############################TOP_OCCUPATIONS####################################################

    output3=open(o1+"_temp1",'w')
    header1 ="TOP_OCCUPATIONS"+ ";" +  "NUMBER_CERTIFIED_APPLICATIONS"  + ";" + "PERCENTAGE"
    output3.write('%s\n' % header1)

    with open(o1+"_temp",'r') as infile:
        counts = collections.Counter(l.strip() for l in infile)
    for line, count in counts.most_common():
        output= line + ";" + str(count) + ";" + str((count/(p-1))*100)+ "%"
        output3.write('%s\n' %output )
    output3.close()

    output4=open(o1, 'w')
    if (len(open(o1+"_temp1").readlines())>=top_int):
        print ("NOTICE: H1bTools using your interesting top OCCUPATIONS\n")
        f=open(o1+"_temp1", 'r')
        for i in range(top_int):
            line=f.next().strip()
            output4.write('%s\n' %line )
            print line
    else:
        print ("\nNOTICE: H1bTools using original top OCCUPATIONS\n")
        l1=len(open(o1+"_temp1").readlines())
        f=open(o1+"_temp1", 'r')
        for i in range(l1):
            line=f.next().strip()
            print line
            output4.write('%s\n' %line )

    output4.close()
    f.close()

##################################TOP_STATES##############################################

    output5=open(o2+"_temp1",'w')
    header2 ="TOP_STATES"+ ";" +  "NUMBER_CERTIFIED_APPLICATIONS"  + ";" + "PERCENTAGE"
    output5.write('%s\n' % header2)

    with open(o2+"_temp",'r') as infile:
        counts = collections.Counter(l.strip() for l in infile)
    for line, count in counts.most_common():
        output= line + ";" + str(count) + ";" + str((count/(p-1))*100)+ "%"
        output5.write('%s\n' %output )
    output5.close()

    output6=open(o2, 'w')
    if (len(open(o2+"_temp1").readlines())>=top_int):
        print ("NOTICE: H1bTools using your interesting top STATES\n")
        f=open(o2+"_temp1", 'r')
        for i in range(top_int):
            line1=f.next().strip()
            print line1
            output6.write('%s\n' %line1)
            
    else:
        print ("\nNOTICE: H1bTools using original top STATES\n")
        l2=len(open(o2+"_temp1").readlines())
        f=open(o2+"_temp1", 'r')
        for i in range(l2):
            line1=f.next().strip()
            print line1
            output6.write('%s\n' %line1)
    output6.close()
    f.close()

   #####################Remove the temparoary files#########################
    os.remove(o1+"_temp")
    os.remove(o2+"_temp")
    os.remove(o1+"_temp1")
    os.remove(o2+"_temp1")

if __name__ == '__main__':
    main()
print ("\nH1bTools finished analysis at %s"  % now )
print("--- %s seconds ---" % (time.time() - start_time))
print ("____________ Good bye ______________")
