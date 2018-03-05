import numpy as np
from rosalind.utilities import read_fasta_dict

def profile(dna):
    length = len(dna[0])
    matrix =  np.zeros((4, length), dtype=np.int)
    for strand in dna:
        for i in range(0, length):
            if strand[i] == "A":
                matrix[0][i] += 1
            elif strand[i] == "C":
                matrix[1][i] += 1
            elif strand[i] == "G":
                matrix[2][i] += 1
            elif strand[i] == "T":
                matrix[3][i] += 1
    return matrix


def consensus(strands):
    matrix = profile(strands)
    # Build consensus from max values in profile columns
    nucleotides = {0: "A", 1: "C", 2: "G", 3: "T"}
    max = np.argmax(matrix, axis=0)
    sequence = ""
    for pos in max:
        sequence += nucleotides[pos]
    return sequence


if __name__ == "__main__":
    file = input("File path: ")
    strands = read_fasta_dict(file)
    dna = [value for value in strands.values()]
    str_profile = profile(dna)
    strA = "A: ";
    strC = "C: ";
    strG = "G: ";
    strT = "T: ";
    for k in range(0, len(dna[0])):
        strA += (str(str_profile[0][k]) + " ");
        strC += (str(str_profile[1][k]) + " ");
        strG += (str(str_profile[2][k]) + " ");
        strT += (str(str_profile[3][k]) + " ");
    print(consensus);
    print(strA);
    print(strC);
    print(strG);
    print(strT);







