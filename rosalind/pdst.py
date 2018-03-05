import numpy as np
from rosalind.utilities import read_fasta_list
from rosalind.hamm import hamming


def pdistance(strings):
    size = len(strings)
    length = len(strings[0])
    D = np.zeros((size, size))
    for x in range(size):
        for y in range(size):
            D[x][y] = hamming(strings[y], strings[x]) / length
    return D


if __name__ == "__main__":
    file = input("File path: ")
    dna = read_fasta_list(file)
    D = pdistance(dna)
    for y in range(len(D)):
        string = ""
        for x in range(len(D)):
            string += str(D[x][y]) + " "
        print(string)



