#!/usr/bin/python
import argparse
import os

## Make commandline arguments with ArgParse
parser = argparse.ArgumentParser()
parser.add_argument("-m", "-material", help="Provide the information type of the directories: nucl (nucleotide / default) or prot (protein)")
parser.add_argument("-o", "-output", help="Provide the names of folders created with GRAB, seperate by commas (no spaces)")
parser.add_argument("-f", "-file", help="Provide file with paths seperated by returns (newlines)")
parser.add_argument("-t", "-title", help="Provide title of blast custom blast database")
args = parser.parse_args()

if args.o != None:
    if args.f != None:
        ## Create an exit point if improper variables are present
        print('Please use only one flag when entering directory names')
        exit()
        
if args.m not in [None, "nucl", "prot"]:
    print("Please enter the type of material in the databases: nucl (nucleotide) or prot (protein)")
    exit()
    
        
## Check for output or file of paths
if args.t == None:
    if args.o == None:
        if args.f == None:
            if os.path.exists("GRAB_Output/"):

                if args.m == "prot":
                    ## Check if Genomes are zipped
                    os.system('ls GRAB_Output/Proteins/ | head -n 1 > tmp')
                    x = open('tmp', 'r').read()
                    os.remove('tmp')
                    x = x.strip()
                    y = x[-2:]
                    ## Unzip genomes if necessary
                    if y == 'gz':
                        os.system('gunzip GRAB_Output/Proteins/*.gz')
                    


                elif args.m in [None, "nucl"]:
                    ## Check if Genomes are zipped
                    os.system('ls GRAB_Output/Nucleotides/ | head -n 1 > tmp')
                    x = open('tmp', 'r').read()
                    os.remove('tmp')
                    x = x.strip()
                    y = x[-2:]

                    ## Unzip genomes if necessary
                    if y == 'gz':
                        os.system('gunzip GRAB_Output/Nucleotides/*.gz')

                        
                os.system('mkdir GRAB_Output/GRAB_DB')

                if args.m == "prot":
                    move_unzipped = 'cat GRAB_Output/Proteins/*.faa > GRAB_Output/GRAB_DB/GRAB_Combined_Proteins.faa'
                    make_db = 'makeblastdb -in GRAB_Output/GRAB_DB/GRAB_Combined_Proteins.faa -dbtype prot -out GRAB_Output/GRAB_DB/GRAB_DB -title "GRAB_DB"'
                else:
                    move_unzipped = 'cat GRAB_Output/Nucleotides/*.fna > GRAB_Output/GRAB_DB/GRAB_Combined_Nucleotides.fna'
                    make_db = 'makeblastdb -in GRAB_Output/GRAB_DB/GRAB_Combined_Nucleotides.fna -dbtype nucl -out GRAB_Output/GRAB_DB/GRAB_DB -title "GRAB_DB"'
                
                    
                os.system(move_unzipped)
                os.system(make_db)
    
            else:
                ## Create an exit point if improper variables are present
                print('Error: Directory: Please enter a directory name from the output of GRAB with -o or -f options or run GRAB.py without naming an output directory before running this script')
                exit()

        if args.f != None:
            my_list = [line.strip().split('\n') for line in open(args.f)]
            my_list = [i[0] for i in my_list]
        
            ## Check if input is present (Watch out for empty newline characters)
            for i in range(0, len(my_list)):
                if os.path.exists(my_list[i]):
                    continue
                else:
                    print('The directory ' + str(my_list[i]) + ' is not found. Please put the output directory of GRAB.py in the same folder as this script')
                    exit()
              ## Create Named Directory
            if os.path.exists("GRAB_Combined/"):
                os.system('rm -r GRAB_Combined/')
            os.system('mkdir GRAB_Combined')

            ## Make directory based on sequence type
            if args.m == "prot":
                mkdir_com = 'mkdir GRAB_Combined/Combined_Proteins'
            else:
                mkdir_com = 'mkdir GRAB_Combined/Combined_Nucleotides'
                
            os.system(mkdir_com)
            os.system('mkdir GRAB_Combined/GRAB_DB')

            ## Check if directories are zipped based on nucelotide status
            if args.m in [None, "nucl"]:
                for i in range(0, len(my_list)):

                    ## Check if Genomes are unzipped
                    check_zip = 'ls ' + str(my_list[i]) + '/Nucleotides/ | head -n 1 > tmp'
                    os.system(check_zip)
                    x = open('tmp', 'r').read()
                    os.remove('tmp')
                    x = x.strip()
                    y = x[-2:]

                    ## Unzip genomes if necessary
                    if y == 'gz':
                        unzip_command = 'gunzip ' + str(my_list[i])+'/Nucleotides/*.gz'
                        os.system(unzip_command)

                    ## Copy and overwrite files to new directory
                    move_command = '\cp -r '+str(my_list[i])+'/Nucleotides/*.fna GRAB_Combined/Combined_Nucleotides/'
                    os.system(move_command)
            else:
                for i in range(0, len(my_list)):

                    ## Check if proteins are unzipped
                    check_zip = 'ls ' + str(my_list[i]) + '/Proteins/ | head -n 1 > tmp'
                    os.system(check_zip)
                    x = open('tmp', 'r').read()
                    os.remove('tmp')
                    x = x.strip()
                    y = x[-2:]

                    ## Unzip proteins if necessary
                    if y == 'gz':
                        unzip_command = 'gunzip ' + str(my_list[i])+'/Proteins/*.gz'
                        os.system(unzip_command)

                    ## Copy and overwrite files to new directory
                    move_command = '\cp -r '+str(my_list[i])+'/Proteins/*.faa GRAB_Combined/Combined_Proteins/'
                    os.system(move_command)
                    



            if args.m == "prot":
                move_unzipped = 'cat GRAB_Combined/Combined_Proteins/*.faa > GRAB_Combined/GRAB_DB/GRAB_Combined_Proteins.faa'
                make_db = 'makeblastdb -in GRAB_Output/GRAB_DB/GRAB_Combined_Proteins.faa -dbtype prot -out GRAB_Output/GRAB_DB/GRAB_DB -title "GRAB_DB"'
            else:
                move_unzipped = 'cat GRAB_Combined/Combined_Nucleotides/*.fna > GRAB_Output/GRAB_DB/GRAB_Combined_Nucleotides.fna'
                make_db = 'makeblastdb -in GRAB_Output/GRAB_DB/GRAB_Combined_Nucleotides.fna -dbtype nucl -out GRAB_Output/GRAB_DB/GRAB_DB -title "GRAB_DB"'
                

            ## Cat Genomes and create fasta
            os.system(move_unzipped)
    
            ## Make BLAST DB
            os.system(make_db)   


        
    if args.o != None:

        my_list = args.o.split(",")
    
        ## Check if input is present
        for i in range(0, len(my_list)):
            if os.path.exists(my_list[i]):
                continue
            else:
                print('The directory ' + str(my_list[i]) + ' is not found. Please put the output directory of GRAB.py in the same folder as this script')
                exit()
    
        ## Create Named Directory
        if os.path.exists("GRAB_Combined/"):
            os.system('rm -r GRAB_Combined/')
        os.system('mkdir GRAB_Combined')

        
        ## Make directory based on sequence type
        if args.m == "prot":
            mkdir_com = 'mkdir GRAB_Combined/Combined_Proteins'
        else:
            mkdir_com = 'mkdir GRAB_Combined/Combined_Nucleotides'
                
        os.system(mkdir_com)
        os.system('mkdir GRAB_Combined/GRAB_DB')
        
       ## Check if directories are zipped based on nucelotide status
        if args.m in [None, "nucl"]:
            for i in range(0, len(my_list)):

                ## Check if Genomes are unzipped
                check_zip = 'ls ' + str(my_list[i]) + '/Nucleotides/ | head -n 1 > tmp'
                os.system(check_zip)
                x = open('tmp', 'r').read()
                os.remove('tmp')
                x = x.strip()
                y = x[-2:]

                ## Unzip genomes if necessary
                if y == 'gz':
                    unzip_command = 'gunzip ' + str(my_list[i])+'/Nucleotides/*.gz'
                    os.system(unzip_command)

                ## Copy and overwrite files to new directory
                move_command = '\cp -r '+str(my_list[i])+'/Nucleotides/*.fna GRAB_Combined/Combined_Nucleotides/'
                os.system(move_command)
        else:
            for i in range(0, len(my_list)):

                ## Check if proteins are unzipped
                check_zip = 'ls ' + str(my_list[i]) + '/Proteins/ | head -n 1 > tmp'
                os.system(check_zip)
                x = open('tmp', 'r').read()
                os.remove('tmp')
                x = x.strip()
                y = x[-2:]

                ## Unzip proteins if necessary
                if y == 'gz':
                    unzip_command = 'gunzip ' + str(my_list[i])+'/Proteins/*.gz'
                    os.system(unzip_command)

                ## Copy and overwrite files to new directory
                move_command = '\cp -r '+str(my_list[i])+'/Proteins/*.faa GRAB_Combined/Combined_Proteins/'
                os.system(move_command)
                    



        if args.m == "prot":
            move_unzipped = 'cat GRAB_Combined/Combined_Proteins/*.faa > GRAB_Combined/GRAB_DB/GRAB_Combined_Proteins.faa'
            make_db = 'makeblastdb -in GRAB_Combined/GRAB_DB/GRAB_Combined_Proteins.faa -dbtype prot -out GRAB_Combined/GRAB_DB/GRAB_DB -title "GRAB_DB"'
        else:
            move_unzipped = 'cat GRAB_Combined/Combined_Nucleotides/*.fna > GRAB_Combined/GRAB_DB/GRAB_Combined_Nucleotides.fna'
            make_db = 'makeblastdb -in GRAB_Combined/GRAB_DB/GRAB_Combined_Nucleotides.fna -dbtype nucl -out GRAB_Combined/GRAB_DB/GRAB_DB -title "GRAB_DB"'
                

        ## Cat Genomes and create fasta
        os.system(move_unzipped)
    
        ## Make BLAST DB
        os.system(make_db)

        
### With Custom DB TITLE


if args.t != None:
    if args.o == None:
        if args.f == None:
            if os.path.exists("GRAB_Output/"):
                name = str(args.t).strip()
                mk_dir = 'mkdir GRAB_Output/' + name
                os.system(mk_dir)
                     ## Check if directories are zipped based on nucelotide status
                if args.m in [None, "nucl"]:
                    for i in range(0, len(my_list)):

                        ## Check if Genomes are unzipped
                        check_zip = 'ls GRAB_Output/Nucleotides/ | head -n 1 > tmp'
                        os.system(check_zip)
                        x = open('tmp', 'r').read()
                        os.remove('tmp')
                        x = x.strip()
                        y = x[-2:]

                        ## Unzip genomes if necessary
                        if y == 'gz':
                            unzip_command = 'gunzip /Nucleotides/*.gz'
                            os.system(unzip_command)
                        
                else:
                    for i in range(0, len(my_list)):
    
                        ## Check if proteins are unzipped
                        check_zip = 'ls ' + str(my_list[i]) + '/Proteins/ | head -n 1 > tmp'
                        os.system(check_zip)
                        x = open('tmp', 'r').read()
                        os.remove('tmp')
                        x = x.strip()
                        y = x[-2:]
        
                        ## Unzip proteins if necessary
                        if y == 'gz':
                            unzip_command = 'gunzip ' + str(my_list[i])+'/Proteins/*.gz'
                            os.system(unzip_command)
                    
                
                if args.m == "prot":
                    move_unzipped = 'cat GRAB_Output/Proteins/*.faa > GRAB_Output/'+name+'/GRAB_Combined_Proteins.faa'
                    make_db =  'makeblastdb -in GRAB_Output/'+name+'/GRAB_Combined_Proteins.faa -dbtype prot -out GRAB_Output/'+name+'/'+name+' -title "'+name+'"'
          
                else:
                    move_unzipped = 'cat GRAB_Output/Nucleotides/*.fna > GRAB_Output/'+name+'/GRAB_Combined_Nucleotides.fna'
                    make_db = 'makeblastdb -in GRAB_Output/'+name+'/GRAB_Combined_Nucleotides.fna -dbtype nucl -out GRAB_Output/'+name+'/'+name+' -title "'+name+'"'
          

                ## Cat Genomes and create fasta
                os.system(move_unzipped)
        
                ## Make BLAST DB
                os.system(make_db)
                    
    
            else:
                ## Create an exit point if improper variables are present
                print('Please enter a directory name from the output of GRAB.py with -o or -f options or run GRAB.py without naming an output directory before running this script')
                exit()

        if args.f != None:
            my_list = [line.strip().split('\n') for line in open(args.f)]
            my_list = [i[0] for i in my_list]
        
            ## Check if input is present (Watch out for empty newline characters)
            for i in range(0, len(my_list)):
                if os.path.exists(my_list[i]):
                    continue
                else:
                    print('The directory ' + str(my_list[i]) + ' is not found. Please put the output directory of GRAB.py in the same folder as this script')
                    exit()
              ## Create Named Directory
            if os.path.exists("GRAB_Combined/"):
                os.system('rm -r GRAB_Combined/')
            os.system('mkdir GRAB_Combined')

             ## Make directory based on sequence type
            if args.m == "prot":
                mkdir_com = 'mkdir GRAB_Combined/Combined_Proteins'
            else:
                mkdir_com = 'mkdir GRAB_Combined/Combined_Nucleotides'
                
            os.system(mkdir_com)
            
            ## Make Directory
            name = str(args.t).strip()
            mk_dir = 'mkdir GRAB_Combined/' + name
            os.system(mk_dir)

            ## Check if directories are zipped based on nucelotide status
            if args.m in [None, "nucl"]:
                for i in range(0, len(my_list)):

                    ## Check if Genomes are unzipped
                    check_zip = 'ls ' + str(my_list[i]) + '/Nucleotides/ | head -n 1 > tmp'
                    os.system(check_zip)
                    x = open('tmp', 'r').read()
                    os.remove('tmp')
                    x = x.strip()
                    y = x[-2:]

                    ## Unzip genomes if necessary
                    if y == 'gz':
                        unzip_command = 'gunzip ' + str(my_list[i])+'/Nucleotides/*.gz'
                        os.system(unzip_command)

                    ## Copy and overwrite files to new directory
                    move_command = '\cp -r '+str(my_list[i])+'/Nucleotides/*.fna GRAB_Combined/Combined_Nucleotides/'
                    os.system(move_command)
            else:
                for i in range(0, len(my_list)):

                    ## Check if proteins are unzipped
                    check_zip = 'ls ' + str(my_list[i]) + '/Proteins/ | head -n 1 > tmp'
                    os.system(check_zip)
                    x = open('tmp', 'r').read()
                    os.remove('tmp')
                    x = x.strip()
                    y = x[-2:]
    
                    ## Unzip proteins if necessary
                    if y == 'gz':
                        unzip_command = 'gunzip ' + str(my_list[i])+'/Proteins/*.gz'
                        os.system(unzip_command)

                    ## Copy and overwrite files to new directory
                    move_command = '\cp -r '+str(my_list[i])+'/Proteins/*.faa GRAB_Combined/Combined_Proteins/'
                    os.system(move_command)
                    

            if args.m == "prot":
                move_unzipped = 'cat GRAB_Combined/Combined_Proteins/*.faa > GRAB_Combined/'+name+'/GRAB_Combined_Proteins.faa'
                make_db =  'makeblastdb -in GRAB_Combined/'+name+'/GRAB_Combined_Proteins.faa -dbtype prot -out GRAB_Combined/'+name+'/'+name+' -title "'+name+'"'
          
            else:
                move_unzipped = 'cat GRAB_Combined/Combined_Nucleotides/*.fna > GRAB_Combined/'+name+'/GRAB_Combined_Nucleotides.fna'
                make_db = 'makeblastdb -in GRAB_Combined/'+name+'/GRAB_Combined_Nucleotides.fna -dbtype nucl -out GRAB_Combined/'+name+'/'+name+' -title "'+name+'"'
          

            ## Cat Genomes and create fasta
            os.system(move_unzipped)
        
            ## Make BLAST DB
            os.system(make_db)

    
                
    if args.o != None:

        my_list = args.o.split(",")
    
        ## Check if input is present
        for i in range(0, len(my_list)):
            if os.path.exists(my_list[i]):
                continue
            else:
                print('The directory ' + str(my_list[i]) + ' is not found. Please put the output directory of GRAB.py in the same folder as this script')
                exit()
    
        ## Create Named Directory
        if os.path.exists("GRAB_Combined/"):
            os.system('rm -r GRAB_Combined/')
            
        os.system('mkdir GRAB_Combined/')

         ## Make directory based on sequence type
        if args.m == "prot":
            mkdir_com = 'mkdir GRAB_Combined/Combined_Proteins'
        elif args.m in [None, "nucl"]:
            mkdir_com = 'mkdir GRAB_Combined/Combined_Nucleotides'
                       
        os.system(mkdir_com)
    
        
        ## Make Directory
        
        name = str(args.t).strip()
        
        mk_dir = 'mkdir GRAB_Combined/' + name
        
        os.system(mk_dir)
        
        ## Check if directories are zipped based on nucelotide status
        if args.m in [None, "nucl"]:
            for i in range(0, len(my_list)):

                ## Check if Genomes are unzipped
                check_zip = 'ls ' + str(my_list[i]) + '/Nucleotides/ | head -n 1 > tmp'
                os.system(check_zip)
                x = open('tmp', 'r').read()
                os.remove('tmp')
                x = x.strip()
                y = x[-2:]

                ## Unzip genomes if necessary
                if y == 'gz':
                    unzip_command = 'gunzip ' + str(my_list[i])+'/Nucleotides/*.gz'
                    os.system(unzip_command)

                ## Copy and overwrite files to new directory
                move_command = '\cp -r '+str(my_list[i])+'/Nucleotides/*.fna GRAB_Combined/Combined_Nucleotides/'
                os.system(move_command)
        else:
            for i in range(0, len(my_list)):

                ## Check if proteins are unzipped
                check_zip = 'ls ' + str(my_list[i]) + '/Proteins/ | head -n 1 > tmp'
                os.system(check_zip)
                x = open('tmp', 'r').read()
                os.remove('tmp')
                x = x.strip()
                y = x[-2:]

                ## Unzip proteins if necessary
                if y == 'gz':
                    unzip_command = 'gunzip ' + str(my_list[i])+'/Proteins/*.gz'
                    os.system(unzip_command)

                ## Copy and overwrite files to new directory
                move_command = '\cp -r '+str(my_list[i])+'/Proteins/*.faa GRAB_Combined/Combined_Proteins/'
                os.system(move_command)
                    



        if args.m == "prot":
            move_unzipped = 'cat GRAB_Combined/Combined_Proteins/*.faa > GRAB_Combined/'+name+'/GRAB_Combined_Proteins.faa'
            make_db =  'makeblastdb -in GRAB_Combined/'+name+'/GRAB_Combined_Proteins.faa -dbtype prot -out GRAB_Combined/'+name+'/'+name+' -title "'+name+'"'
          
        else:
            move_unzipped = 'cat GRAB_Combined/Combined_Nucleotides/*.fna > GRAB_Combined/'+name+'/GRAB_Combined_Nucleotides.fna'
            make_db = 'makeblastdb -in GRAB_Combined/'+name+'/GRAB_Combined_Nucleotides.fna -dbtype nucl -out GRAB_Combined/'+name+'/'+name+' -title "'+name+'"'
          

        ## Cat Genomes and create fasta
        os.system(move_unzipped)
    
        ## Make BLAST DB
        os.system(make_db)
