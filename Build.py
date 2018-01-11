#!/usr/bin/python
import argparse
import os


## Make commandline arguments with ArgParse
parser = argparse.ArgumentParser()
parser.add_argument("-o", "-output", help="Provide the names of folders created with GRAB, seperate by commas")
parser.add_argument("-f", "-file", help="Provide file with paths seperated by returns")
parser.add_argument("-t", "-title", help="Provide title of blast custom blast database")
args = parser.parse_args()


## Check for output or file of paths
if args.o == None:
    if args.f == None:
        if os.path.exists("GRAB_Output/"):
            os.system('gunzip GRAB_Output/Genomes/*.gz')
            os.system('mkdir GRAB_Output/GRAB_DB')
            os.system('cat GRAB_Output/Genomes/*.fna > GRAB_Output/GRAB_DB/GRAB_Combined_Genomes.fasta')
            os.system('makeblastdb -in GRAB_Output/GRAB_DB/GRAB_Combined_Genomes.fasta -dbtype nucl -out GRAB_Output/GRAB_DB/GRAB_DB -title "GRAB_DB"')
            
        else:
            ## Create an exit point if improper variables are present
            print('Please enter a directory name from the output of GRAB with -o or -f options or run GRAB without naming an output directory')
            exit()

    if args.f != None:
        my_list = [ line.strip().split('\n') for line in open(args.f)]
        my_list = [i[0] for i in my_list]
        ## Work More Here

        
if args.o != None:
    my_list = args.o.split(",")

    ## Check if input is present
    for i in range(0, len(my_list)):
        if os.path.exists(my_list[i]):
            continue
        else:
            print('The directory ' + str(my_list[i]) + ' is not found. Please put the output directory of GRAB in the same folder as this script')

    ## 

    
    



##

#makeblastdb -in input_reads -dbtype nucl -out output_name -title "Title here"
#os.system
