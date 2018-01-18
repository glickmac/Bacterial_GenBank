# GRAB

## Table of Contents
[What is GRAB?](#intro)    
[Why is this important?](#importance)    
[GRAB Workflow](#workflow)    
[Quickstart](#quickstart)    
[Installing GRAB](#install)    
[GRAB Usage](#usage)    
[GRAB Testing and Validation](#testing_and_validation)    
[Additional Functionality](#additional)    

## <a name="intro"></a>What is GRAB?

GRAB is short for Genomic Retrieval and Blast Database Creation. Grab consists of python scripts to mine the NCBI FTP sites for genomes, coding regions, or proteins of interest. 

## <a name="importance"></a>Why is this important?

GRAB automates the retrieval of genomic information to build custom BLAST databases. The current method of finding genomic information is laborious and time intensive and human error may result in missed information. GRAB provides an automated system to overcome current limitations in creating custom databases. 

## <a name="workflow"></a>GRAB Workflow

<img src="https://github.com/NCBI-Hackathons/VirusCore/blob/master/workflow.png" height="450" width="650">


### Useful References

#### Anaconda 
[Anaconda](https://www.anaconda.com) 
Anaconda is a package manager to run GRAB on most systems

#### Bioconda
[Bioconda](https://bioconda.github.io/)
Bioconda is a channel that includes import packages notably BLAST

#### BLAST
[BLAST Command Line Manual](https://www.ncbi.nlm.nih.gov/books/NBK279690/)
The scripts are split to allow a user to create a BLAST database their own way
 
[BLAST Formatting](https://www.biostars.org/p/88944/)  
A helpful post on BLAST database formatting   
   

## <a name="install"></a>Installing GRAB

Required software
+ Anaconda: [download](https://www.anaconda.com/download/) [documentation](https://conda.io/docs/user-guide/tasks/manage-environments.html)
+ Bioconda: Install after Anaconda with commands below

```
conda config --add channels defaults
conda config --add channels conda-forge
conda config --add channels bioconda
```

#### Download GRAB
[GRAB Download]()

Create the environment from the GRAB_environment.yml file:

```
conda env create -f GRAB_environment.yml
```
Activate the new environment:

Windows: activate myenv
macOS and Linux: source activate myenv
NOTE: Replace myenv with the name of the environment.







conda list

+ [BLAST+](https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download)
+ [Samtools](http://www.htslib.org/) (>= version 1.5)
+ [Prinseq](http://prinseq.sourceforge.net/)
+ [MEGAHIT](https://github.com/voutcn/megahit)
+ [Glimmer3](https://ccb.jhu.edu/software/glimmer/)



## <a name="usage"></a><a name="quickstart"></a>GRAB Usage

#### Example usage

```
viruspy.sh [-d] [-f viral_genomes.fasta/-b viral_db] -s SRR1553459 -o output_folder
```

#### Required arguments:

| Option     | Description                                     |
|------------|-------------------------------------------------|
| **-s**   | SRR acession number from SRA database           |
| **-o**   | Folder to be used for pipeline output |

#### Optional arguments:

| Option    | Description |
|-----------|-------------|
| **-f**    |FASTA file containing viral sequences to be used in construction of a BLAST database. If neither this argument nor -b are used, ViruSpy will default to using the Refseq viral genome database.|
| **-b**    |BLAST database with viral sequences to be used with Magic-BLAST. If neither this argument nor -f are used, ViruSpy will default to using the Refseq viral genome database.|
| **-d**    |Determines signature of viruses that are integrated into a host genome (runs the BUD algorithm)|

## <a name="testing_and_validation"></a>ViruSpy Testing and Validation

### Edge Cases
Myco + Bact avium example for edge case

## <a name="additional"></a>Additional Functionality
