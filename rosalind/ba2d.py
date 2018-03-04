import numpy as np

from rosalind.hamm import hamming
from rosalind.cons import consensus, profile
from rosalind.ba2c import pp_kmer


def score(motifs):
    seq = consensus(motifs)
    s = 0
    for motif in motifs:
        s += hamming(motif, seq)
    return s


def greedy_motif_search(dna, k, t):
    best_motifs = [string[:k] for string in dna];
    length = len(dna[0]);
    for i in range(length - k + 1):
        motifs = [];
        motifs.append(dna[0][i:i + k]);
        for j in range(1, t):
            p = profile(motifs[0:j])/len(motifs[0:j]);
            motifs.append(pp_kmer(dna[j], k, p));
        if score(motifs) < score(best_motifs):
            best_motifs = motifs;
    return best_motifs;


if __name__ == "__main__":
    file = input("File path: ")
    with open(file) as input:
        values = input.readline().strip().split(" ")
        k, t = int(values[0]), int(values[1])
        dna = []
        strand = input.readline().strip()
        while strand:
            dna.append(strand)
            strand = input.readline().strip()
    for motif in greedy_motif_search(dna, k, t):
        print(motif)