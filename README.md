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

ViruSpy is a pipeline designed for virus 

## <a name="importance"></a>Why is this important?

Viruses compose a large amount of the genomic biodiversity on the planet, but only a small fraction of the viruses that exist are known. 

## <a name="workflow"></a>GRAB Workflow

<img src="https://github.com/NCBI-Hackathons/VirusCore/blob/master/workflow.png" height="450" width="650">


### Useful References

#### Magic-BLAST

[BLAST Command Line Manual](https://www.ncbi.nlm.nih.gov/books/NBK279690/)    
[Magic-BLAST GitHub repo](https://github.com/boratyng/magicblast)    
[Magic-BLAST NCBI Insights](https://ncbiinsights.ncbi.nlm.nih.gov/2016/10/13/introducing-magic-blast/)    

#### MEGAHIT

[MEGAHIT GitHub repo](https://github.com/voutcn/megahit)    
[MEGAHIT Paper](https://www.ncbi.nlm.nih.gov/pubmed/25609793)    
   

## <a name="install"></a>Installing GRAB

Required software
+ Magic-BLAST (>= v1.3): [download](https://ftp.ncbi.nlm.nih.gov/blast/executables/magicblast/LATEST) [documentation](https://boratyng.github.io/magicblast/)
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
