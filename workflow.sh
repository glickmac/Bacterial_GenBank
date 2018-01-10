#!/bin/bash
set -euo pipefail  # bash strict mode http://redsymbol.net/articles/unofficial-b$
IFS=$'\n\t'

main_dir=$(pwd)
threads=4

usage() { echo "$0 parameters:" && grep "[[:space:]].)\ #" $0 | sed 's/#//'; exit 0; }

while getopts ":hq:f:l:o:" option
do
case "${option}" in
        q) # A comma seperated list of full or partial organism names at a single taxonomic level (Use q or f, but not both)
		query=${OPTARG};;

        f) # The location of a text file containing the full or partial names of organisms (Use q or f, but not both)
		filename=${OPTARG};;

	l) # The taxonomic level to filter bacteria 
		level=${OPTARG};;

	o) # The output directory of the sequences
		output=${OPTARG} || "BTD_Output";;

        h | *) # Display Help
                usage
                exit 0;;
esac
done

shift "$((OPTIND-1))"

echo $output
