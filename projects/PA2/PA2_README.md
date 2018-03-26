# Programming Assignment 2


## Getting Started
You should be able to integrate your code from last week

## Instructions
You will have to start thinking about insertions and deletions now, but your first job is still to write code that does a good job of identifying SNPs.  The most important thing you'll have to worry about on this assignment is speed; your code can end up going too slowly if you don't implement some optimizations.

## Outline of Provided Skeleton Code
The hasher only changes the speed at which you're going to get aligned reads, but it's also going to provide a bit more complicated output that you'll have to disentangle to 

## What You Should Change
Play with the basic hasher. Think about what it does well and does poorly. Try it out on the larger datasets.

What's a good choice for the key length here?

## My Implementation

*NW_align* implements a Needleman_Wunsch type algorithm and matrix backtracking to globally align the donor genome. The data was initially aligned using *genome_align* from PA1. The NW_align was then used to distinguish between SNPS and INDEL variants. 

This implementation received a score of 82.06% on SNP and 15.45% on INDEL identifications on the [Course Score Board](https://cm124.herokuapp.com/view_hw2_scores) 
