#!/usr/bin/python
import argparse
import pandas as pd
import os

## Make commandline arguments with ArgParse
parser = argparse.ArgumentParser()
parser.add_argument("-q", "-query", help="Provide the full or partial name of the organisms you want to download, seperate by commas")
parser.add_argument("-f", "-file", help="Provide file with full or partial names seperated by returns")
parser.add_argument("-l", "-level", help="Provide the taxonomic level you wish to query: Options include Phylum, Order, Class, Family, Genus, Species, Subspecies")
parser.add_argument("-o", "-output", help="Provide output directory name to store sequences")
args = parser.parse_args()


## Load in two dataframes (Assemblies and taxid2linage)
assembly_summary = pd.read_table('data/assembly_summary.txt', keep_default_na=False, na_values=[""])
bacterial_taxa = pd.read_csv('data/Bacterial_tax_id_Levels.csv', keep_default_na=False, na_values=[""])


## Merge dataframes by tax_id
merged_inner = pd.merge(left=assembly_summary, right=bacterial_taxa, left_on='taxid', right_on='tax_id')
merged_inner.subspecies = merged_inner.subspecies.astype(str)

## Clean_up dataframe

### Currently the filtering by taxonomy relies on the column number so this
### section remains a to-do priority. The numbers in Define Taxonomic will need
### to be adjusted for the filtered table to be created 


## Define GREP Function
def _grep(x, list_to_grep):
    for text in list_to_grep:
        if text.lower() in x.lower():
            return True
    return False

if args.l == None:
    ## Create an exit point if improper variables are present
    print('Please enter a taxanomic level with the -l flag: Phylum, Class, Order, Family, Genus, Species, or Subspecies')
    exit()

    
## Define Taxonomic Category
if args.l.lower() == 'phylum':
    col_num = 23
elif args.l.lower() == 'class':
    col_num = 24
elif args.l.lower() == 'order':
    col_num = 25
elif args.l.lower() == 'family':
    col_num = 26
elif args.l.lower() == 'genus':
    col_num = 27
elif args.l.lower() == 'species':
    col_num = 28
elif args.l.lower() == 'subspecies':
    col_num = 29
else:
    ## Create an exit point if improper variables are present
    print('Please enter a taxanomic level with the -l flag: Phylum, Class, Order, Family, Genus, Species, or Subspecies')
    exit()

## Make Directory
if args.o == None:
    if os.path.exists("GRAB_Output"):
        os.system('rm -r GRAB_Output')
        os.system('mkdir GRAB_Output')
    else:
        os.system('mkdir GRAB_Output')
    
    
if args.o != None:
    if os.path.exists(str(args.o)):
        name = 'mkdir '+str(args.o)
        rm_name = 'rm -r '+str(args.o)
        os.system(rm_name)
        os.system(name)
    else:
        name = 'mkdir '+str(args.o)
        os.system(name)
         
## Decide which flag is used
if args.q != None:
    if args.f != None:
        print('Please only use one arugment flag (-q or -f) in this version')
        exit()


if args.f == None:
    ## Create an exit point if improper varaibles are present
    if args.q == None:
        print('Please enter a -q query flag or -f filename flag with full or partial organisms to download')
        exit()
    else:
        my_list = args.q.split(",")
        mask = merged_inner.iloc[:,col_num].apply(_grep, list_to_grep = my_list)
        test = merged_inner[mask]
        ## Clean up data table
     
        if args.o == None:
            test.to_csv('GRAB_Output/filtered_table.txt',sep='\t')
        else:
            output = str(args.o)+'/filtered_table.txt'
            test.to_csv(output,sep='\t')
    
if args.q == None:
    my_list = [ line.strip().split('\n') for line in open(args.f)]
    my_list = [i[0] for i in my_list]
    mask = merged_inner.iloc[:,col_num].apply(_grep, list_to_grep = my_list)
    test = merged_inner[mask]
    ## Clean up data table
    
    if args.o == None:
        test.to_csv('GRAB_Output/filtered_table.txt',sep='\t')
    else:
        output = str(args.o)+'/filtered_table.txt'
        test.to_csv(output,sep='\t')



## Default Directory Name
if args.o == None:
    ## Run Awk command to check for complete genomes
    os.system('''awk -F '\t' '{if($13=="Complete Genome") print $21}' GRAB_Output/filtered_table.txt > GRAB_Output/filtered_addresses.txt''')

    ## Genome Names
    os.system('''awk -F '\t' '{if($13=="Complete Genome") print $2,$26,$27,$28,$29,$30,$31,$32}' GRAB_Output/filtered_table.txt > GRAB_Output/genome_names.txt''')
    ## Make new directory
    os.system('mkdir GRAB_Output/Genomes')

    with open('GRAB_Output/filtered_addresses.txt', 'r') as f:
        wgets = f.readlines()


    print('Downloading ' + str(len(wgets)) + ' complete genomes into genomes folder...this may take a while')
          
    for i in range(0,len(wgets)):
        ## loop to format and call wget
        wlink = str(wgets[i])
        wlink = wlink.replace('\n','')

        ## Split the genome to recieve only genomic information
        wsplit = wlink.split('/')
        genome = str(wsplit[9])
        genome = genome.replace('\n', '')

        ## Create new system call
        new_wget = 'wget -P GRAB_Output/Genomes '+wlink+'/'+genome+'_genomic.fna.gz -q --show-progress'
        os.system(new_wget)



## Custom Directory Name
if args.o != None:
    ## Run Awk command to check for complete genomes
    awk_name = '''awk -F '\t' '{if($13=="Complete Genome") print $21}' '''+str(args.o)+'/filtered_table.txt > '+str(args.o)+'/filtered_addresses.txt'
    os.system(awk_name)


    genome_name = '''awk -F '\t' '{if($13=="Complete Genome") print $2,$26,$27,$28,$29,$30,$31,$32}' '''+str(args.o)+'/filtered_table.txt > '+str(args.o)+'/genome_names.txt'
    os.system(genome_name)
    ## Make new directory
    dir_name = 'mkdir '+str(args.o)+'/Genomes'
    os.system(dir_name)


    dir_address = str(args.o)+'/filtered_addresses.txt'
    dir_location = str(args.o)+'/Genomes '
    with open(dir_address, 'r') as f:
          wgets = f.readlines()


    print('Downloading ' + str(len(wgets)) + ' complete genomes into genomes folder...this may take a while')
          
    for i in range(0,len(wgets)):
        ## loop to format and call wget
        wlink = str(wgets[i])
        wlink = wlink.replace('\n','')

        ## Split the genome to recieve only genomic information
        wsplit = wlink.split('/')
        genome = str(wsplit[9])
        genome = genome.replace('\n', '')

        ## Create new system call
        new_wget = 'wget -P '+dir_location+wlink+'/'+genome+'_genomic.fna.gz -q --show-progress'
        os.system(new_wget)


               
def main():
    pass
    
