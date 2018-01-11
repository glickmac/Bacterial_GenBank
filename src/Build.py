#!/usr/bin/python
import argparse
import os


## Make commandline arguments with ArgParse
parser = argparse.ArgumentParser()
parser.add_argument("-o", "-output", help="Provide the names of folders created with GRAB, seperate by commas")
parser.add_argument("-f", "-file", help="Provide file with paths seperated by returns")
parser.add_argument("-t", "-title", help="Provide title of blast custom blast database")
args = parser.parse_args()


##



##

#makeblastdb -in input_reads -dbtype nucl -out output_name -title "Title here"
#os.system
