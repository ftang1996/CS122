# CS 122
UCLA CS122 with Eskin, Winter 2018


## Project 1

### Overview
In the first two programming assignments for this class, you will solve the computational problem of re- sequencing, which is the process of inferring a donor genome based on reads and a reference.
You are given a reference genome in FASTA format, and paired-end reads.
The first line of each file indicates which project that the data relates to. In the reference file, the genome is written in order, 80 bases (A’s, C’s, G’s, and T’s) per line.
The paired end reads are generated from the unknown donor sequence, and 10 percent of the reads are generated randomly to mimic contamination with another genetic source. These reads are formatted as two 50 bp-long ends, which are separated by a 90-110 bp-long separator.

### Getting Started
If you've set everything up correctly, you should have no trouble running
*basic_aligner.py* and *basic_pileup.py* to get some properly formatted output
which you can submit on the [course site](https://cm124.herokuapp.com)

### Instructions
Don't worry about insertions and deletions for this project. All you need to do is figure out how to tell the true SNPs from the false positives in the consensus sequence.

### Outline of Provided Skeleton Code
The reference and reads are the inputs to *basic_aligner.py*, which are converted to the aligned file using a trivial alignment algorithm.

The aligned data is fed into the *basic_pileup.py* script, which generates a consensus sequence by picking the most common base at each position.  That "consensus" file is the heart of this assignment; it has the reference, the aligned reads, and then an asterisk at every position where the consensus sequence differs from the reference. If you can understand what is going on there, you'll understand what you can change to improve mapping true SNPs, and then go on to mapping structural variations.

The *basic_pileup.py* script also makes a file that starts snps that is used to format the output properly.  It notes all of the differences between the consensus and the reference and notes the position where they occur. It also zips that file so you can sumbit it directly to the course site.

### My Implementation

*genome_align* implements a hashing algorithm to construct a table of kmers for the reference genome. This significantly improves speeds compared to the skeleton *basic_aligner*, as the process simply looks up possible alignments for a read with a minimum number of mismatches, instead of scanning through every possible match. 

This implementation received a score of 87.5% on SNP identifications on the [Course Score Board](https://cm124.herokuapp.com/view_hw1_scores) 


## Project 2
### Getting Started
You should be able to integrate your code from last week

### Instructions
You will have to start thinking about insertions and deletions now, but your first job is still to write code that does a good job of identifying SNPs.  The most important thing you'll have to worry about on this assignment is speed; your code can end up going too slowly if you don't implement some optimizations.

### Outline of Provided Skeleton Code
The hasher only changes the speed at which you're going to get aligned reads, but it's also going to provide a bit more complicated output that you'll have to disentangle to 

### What You Should Change
Play with the basic hasher. Think about what it does well and does poorly. Try it out on the larger datasets.

What's a good choice for the key length here?

### My Implementation

*NW_align* implements a Needleman_Wunsch type algorithm and matrix backtracking to globally align the donor genome. The data was initially aligned using *genome_align* from PA1. The NW_align was then used to distinguish between SNPS and INDEL variants. 

This implementation received a score of 82.06% on SNP and 15.45% on INDEL identifications on the [Course Score Board](https://cm124.herokuapp.com/view_hw2_scores) 


## Rosalind HW
ASMQ
- Problem Title:Assessing Assembly Quality with N50 and N75
- URL: http://rosalind.info/problems/asmq

BA1E
- Problem Title: Find Patterns Forming Clumps in a String
- URL: http://rosalind.info/problems/ba1e

BA1F
- Problem Title: Find a Position in a Genome Minimizing the Skew
- URL: http://rosalind.info/problems/ba1f

BA1H
- Problem Title: Find All Approximate Occurrences of a Pattern in a String
- URL: http://rosalind.info/problems/ba1h

BA2B 
- Problem Title: Find a Median String
- URL: http://rosalind.info/problems/ba2b

BA2C
- Problem Title: Implement GreedyMotifSearch
- URL: http://rosalind.info/problems/ba2c

BA2D
- Problem Title: Find a Profile-most Probable k-mer in a String
- URL: http://rosalind.info/problems/ba2d

BA3C
- Problem Title: Construct the Overlap Graph of a Collection of k-mers
- URL: http://rosalind.info/problems/ba2d

BA5A:
- Problem Title: Find the Minimum Number of Coins Needed to MakeChange
- URL: http://rosalind.info/problems/ba5a

BA5C
- Problem Title: Find a Longest Common Subsequence of Two Strings
- URL: http://rosalind.info/problems/ba5c

BA5G
- Problem Title: Compute the Edit Distance Between Two Strings
- URL: http://rosalind.info/problems/ba5g

BA9B
- Problem Title: Implement TrieMatching
- URL: http://rosalind.info/problems/ba9b

BA9I
- Problem Title: Construct the Burrows-Wheeler Transform of a String
- URL: http://rosalind.info/problems/ba9b

CONS
- Problem Title: Consensus and Profile
- URL: http://rosalind.info/problems/cons

CORR
- Problem Title: Error Correction in Reads
- URL: http://rosalind.info/problems/corr

DBRU
- Problem Title: Constructing a De Bruijn Graph
- URL: http://rosalind.info/problems/dbru

DEG
- Problem Title: Degree Array
- URL: http://rosalind.info/problems/corr

DNA
- Problem Title: Counting DNA Nucleotides
- URL: http://rosalind.info/problems/dna

FIB
- Problem Title: Rabbits and Recurrence Relations
- URL: http://rosalind.info/problems/fib

GASM
- Problem Title: Genome Assembly Using Reads
- URL: http://rosalind.info/problems/gasm

GC
- Problem Title: Genome Assembly with Perfect Coverage and Repeats
- URL: http://rosalind.info/problems/gc

GREP
- Problem Title: Computing GC Content
- URL: http://rosalind.info/problems/grep

HAMM
- Problem Title: Counting Point Mutations
- URL: http://rosalind.info/problems/hamm

HDAG
- Problem Title: Hamiltonian Path in DAG
- URL: http://rosalind.info/problems/hdag

IEV
- Problem Title: Calculating Expected Offspring
- URL: http://rosalind.info/problems/iev

IPBR
- Problem Title: Mendel's First Law
- URL: http://rosalind.info/problems/ipbr

INI3
- Problem Title: Strings and Lists
- URL: http://rosalind.info/problems/ini3

INI5
- Problem Title: Working with Files
- URL: http://rosalind.info/problems/ini5

INI6
- Problem Title: Dictionaries
- URL: http://rosalind.info/problems/ini6

MRNA
- Problem Title: Inferring mRNA from Protein
- URL: http://rosalind.info/problems/mrna

PCOV
- Problem Title: Genome Assembly with Perfect Coverage
- URL: http://rosalind.info/problems/pcov

PDST
- Problem Title: Creating a Distance Matrix
- URL: http://rosalind.info/problems/pdst

PROB
- Problem Title: Introduction to Random Strings
- URL: http://rosalind.info/problems/prob

PROT
- Problem Title: Translating RNA into Protein
- URL: http://rosalind.info/problems/prot

REVC
- Problem Title: Complementing a Strand of DNA
- URL: http://rosalind.info/problems/revc



