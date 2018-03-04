import math

from rosalind.hamm import hamming
from rosalind.ba1e import to_nucleotide, to_pattern


""" Return minimum hamming distance over all strands """
def pattern_distance(pattern, dna):
    k = len(pattern)
    distance = 0
    for strand in dna:
        substrings = [strand[i:i + k] for i in range(len(strand) - k + 1)]
        min_ham = min(map(lambda x: hamming(pattern, x), substrings))
        distance += min_ham
    return distance


def median_string(dna, k):
    min_distance = math.inf
    for i in range(4 ** k - 1):
        pattern = to_pattern(i, k)
        distance = pattern_distance(pattern, dna)
        if min_distance > distance:
            min_distance = distance
            median = pattern
    return median


if __name__ == "__main__":
    file = input("File path: ")
    with open(file) as input:
        k = int(input.readline().strip())
        dna = input.readlines()
        dna = [line.strip() for line in dna]
    print(median_string(dna, k))

