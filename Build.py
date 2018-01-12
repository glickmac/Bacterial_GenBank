#!/usr/bin/python
import argparse
import os

## Make commandline arguments with ArgParse
parser = argparse.ArgumentParser()
parser.add_argument("-o", "-output", help="Provide the names of folders created with GRAB, seperate by commas")
parser.add_argument("-f", "-file", help="Provide file with paths seperated by returns")
parser.add_argument("-t", "-title", help="Provide title of blast custom blast database")
args = parser.parse_args()

if args.o != None:
    if args.f != None:
        ## Create an exit point if improper variables are present
        print('Please use only one flag when entering direcoty names')
        exit()

        
## Check for output or file of paths
if args.o == None:
    if args.f == None:
        if os.path.exists("GRAB_Output/"):
            
            ## Check if Genomes are zipped
            os.system('ls GRAB_Output/Genomes/ | head -n 1 > tmp')
            x = open('tmp', 'r').read()
            os.remove('tmp')
            x = x.strip()
            y = x[-2:]

            ## Unzip genomes if necessary
            if y == 'gz':
                os.system('gunzip GRAB_Output/Genomes/*.gz')
            os.system('mkdir GRAB_Output/GRAB_DB')
            os.system('cat GRAB_Output/Genomes/*.fna > GRAB_Output/GRAB_DB/GRAB_Combined_Genomes.fasta')
            os.system('makeblastdb -in GRAB_Output/GRAB_DB/GRAB_Combined_Genomes.fasta -dbtype nucl -out GRAB_Output/GRAB_DB/GRAB_DB -title "GRAB_DB"')
    
        else:
            ## Create an exit point if improper variables are present
            print('Please enter a directory name from the output of GRAB with -o or -f options or run GRAB.py without naming an output directory before running this script')
            exit()

    if args.f != None:
        my_list = [ line.strip().split('\n') for line in open(args.f)]
        my_list = [i[0] for i in my_list]

        ## To-Do Files

        
if args.o != None:

    my_list = args.o.split(",")
    
    ## Check if input is present
    for i in range(0, len(my_list)):
        if os.path.exists(my_list[i]):
            continue
        else:
            print('The directory ' + str(my_list[i]) + ' is not found. Please put the output directory of GRAB in the same folder as this script')
            exit()
    
    ## Create Named Directory
    if os.path.exists("GRAB_Combined/"):
        os.system('rm -r GRAB_Combined/')
    os.system('mkdir GRAB_Combined')
    os.system('mkdir GRAB_Combined/Combined_Genomes')
    os.system('mkdir GRAB_Combined/GRAB_DB')
    
    for i in range(0, len(my_list)):

        ## Check if Genomes are unzipped
        check_zip = 'ls ' + str(my_list[0]) + '/Genomes/ | head -n 1 > tmp'
        os.system(check_zip)
        x = open('tmp', 'r').read()
        os.remove('tmp')
        x = x.strip()
        y = x[-2:]

        ## Unzip genomes if necessary
        if y == 'gz':
            unzip_command = 'gunzip ' + str(my_list[i])+'/Genomes/*.gz'
            os.system(unzip_command)

        ## Copy and overwrite files to new directory
        move_command = '\cp -r '+str(my_list[i])+'/Genomes/*.fna GRAB_Combined/Combined_Genomes/'
        os.system(move_command)


    ## Cat Genomes and create fasta
    os.system('cat GRAB_Combined/Combined_Genomes/*.fna > GRAB_Combined/GRAB_DB/GRAB_Combined_Genomes.fasta')

    ## Make BLAST DB
    os.system('makeblastdb -in GRAB_Combined/GRAB_DB/GRAB_Combined_Genomes.fasta -dbtype nucl -out GRAB_Combined/GRAB_DB/GRAB_DB -title "GRAB_DB"')   
    



