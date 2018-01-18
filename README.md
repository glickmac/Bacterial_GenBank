# GRAB

## Table of Contents
[What is GRAB?](#intro)    
[Why is this important?](#importance)    
[GRAB Workflow](#workflow)    
[Quickstart](#quickstart)    
[Installing GRAB](#install)    
[GRAB Usage](#usage)    
[GRAB Examples with Pictures](#testing_and_validation)    
[Additional Functionality](#additional)    

## <a name="intro"></a>What is GRAB?

GRAB is short for Genomic Retrieval and Blast Database Creation. GRAB currently is only able to mine **bacterial** genomic information by taxonomy. GRAB consists of python scripts to mine the NCBI FTP sites for genomes, coding regions, or proteins of interest. 

## <a name="importance"></a>Why is this important?

GRAB automates the retrieval of genomic information to build custom BLAST databases. The current method of finding genomic information is laborious and time intensive and human error may result in missed information. GRAB provides an automated system to overcome current limitations in creating custom databases. 

## <a name="workflow"></a>GRAB Workflow

<img src="https://github.com/NCBI-Hackathons/VirusCore/blob/master/workflow.png" height="450" width="650">


### Useful References

[Anaconda](https://www.anaconda.com)

Anaconda is a package manager to run GRAB on most systems

[Bioconda](https://bioconda.github.io/)

Bioconda is a channel that includes import packages notably BLAST

#### BLAST

[BLAST Command Line Manual](https://www.ncbi.nlm.nih.gov/books/NBK279690/)

The scripts are split to allow a user to create a BLAST database their own way
 
[BLAST makeblastdb Example](https://www.haktansuren.com/blast-makeblastdb/) 

A helpful post on BLAST command makeblastdb 
   

## <a name="install"></a>Installing GRAB

Required software
+ Anaconda: 
[download](https://www.anaconda.com/download/) || [environment documentation](https://conda.io/docs/user-guide/tasks/manage-environments.html)

+ Bioconda: Install after Anaconda with commands below

```
conda config --add channels defaults
conda config --add channels conda-forge
conda config --add channels bioconda
```

### [Download GRAB](https://github.com/glickmac/GRAB/raw/master/GRAB.zip)

#### Unzip GRAB and CD into Directory

```
unzip GRAB.zip
cd GRAB
```

#### Create the environment from the GRAB_environment.yml file:

```
conda env create -f GRAB_environment.yml
```
Activate the new environment:

Windows: activate myenv
macOS and Linux: source activate myenv
NOTE: Replace myenv with the name of the environment.

#### Other installations (Git)

```
git clone https://github.com/glickmac/GRAB
```


## <a name="usage"></a><a name="quickstart"></a>GRAB Usage

GRAB consists of two python scripts. One to pull genomic, coding regions, or proteins from bacteria of choice and another to automatically build a database. 

+ GRAB.py Help: 

```
python GRAB.py -h
```

+ Build.py Help: 

```
python Build.py -h
```

### GRAB.py (Information Retrieval from NCBI)

Either -q or -f is required, however please use only one flag at a time

#### Required arguments :

| Option     | Description                                     |
|------------|-------------------------------------------------|
| **-q** or **-f**   | -q: -query seperated by commas **(no spaces)** or -f: -file with query seperated by new lines  |
| **-l**   | -level: Taxanomic level: options include *phylum, order, class, family, genus, species, or subspecies*  |

#### Optional arguments:

| Option    | Description |
|-----------|-------------|
| **-m**    |-material: Material to download from NCBI FTP: options include *genomic* **(DEFAULT)**, *coding* (DNA Coding regions), *protein* (Proteins)|
| **-o**    |-output: Create a custom output directory for retrieval, GRAB_Output **(DEFAULT)** |


### Build.py (Automated BLAST Database Creation)

Either -o or -f is required, however please use only one flag at a time. The -o option specifies the output name of GRAB.py

#### Required arguments :

| Option     | Description                                     |
|------------|-------------------------------------------------|
| **-o** or  **-f**    | -o: -output of GRAB.py seperated by commas **(no spaces)** or -f: -file with GRAB.py outputs seperated by new lines  |

#### Optional arguments:

| Option    | Description |
|-----------|-------------|
| **-m**    |-material: Material to build database: options include *nucl* (Nucleotide, **DEFAULT**), *prot* (Proteins)|
| **-t**    |-title: Create a custom name for database, GRAB_DB **(DEFAULT)** |


## <a name="testing_and_validation"></a>GRAB Examples with Pictures

GRAB currently operates only in the GRAB directory. The directories from GRAB.py are needed to run Build.py. You can remove the BLAST database (GRAB_DB is the default) created by Build.py and use it as a functional [blast db](https://www.biostars.org/p/88944/) for blastn, blastx, tblastx, blastp. 

### GRAB.py 

#### Query flag
The query flag can take more than one input seperated by commas. Here we search for two subspecies of Mycobacterium abscessus: massiliense and boletti

```
python GRAB.py -q massiliense,boletti -l subspecies
```

Output: 

The default output directory is **GRAB_Output** 


The directory contains a folder Nucleotides and three text files. Taxonomy names is a good file to check the retrieval was successful






## <a name="additional"></a>Edge Cases

### Edge Cases
Myco + Bact avium example for edge case
