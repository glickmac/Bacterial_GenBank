#!/usr/bin/python
import os

with open('../BDT_Output/filtered_addresses.txt', 'r') as f:
    wgets = f.readlines()



for i in range(0,len(wgets)):
    ## loop to format and call wget
    wlink = wgets[i]
    wlink = wlink.replace('\n','')

    ## Split the genome to recieve only genomic information
    wsplit = wlink.split('/')
    genome = wsplit[9]
    genome = genome.replace('\n', '')

    ## Create new system call
    new_wget = 'wget -P ..BDT_Output/Genomes '+test+'/'+genome+'_genomic.fna.gz'
    os.system(new_wget)
 



def main():
    pass
