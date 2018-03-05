import collections
from rosalind.utilities import read_fasta_dict
from rosalind.hamm import hamming
from rosalind.revc import rev_complement

# s -> (s0,s1), (s1,s2), (s2, s3), ...
def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def correct_reads(reads):
    # Make array of reverse complements
    reverse = list(map(rev_complement, reads))

    # Find correct strands
    count = collections.Counter(reads)
    for strand in reverse:
        if strand in count:
            count[strand] += 1
    correct, incorrect = [], []
    for key in count:
        if count[key] > 1:
            correct.append(key)
        else:
            incorrect.append(key)
    rev_correct = list(map(rev_complement, correct))

    # Corrected read if hamming distance = 1 for strand or rev complement
    corrected = {}
    for item in incorrect:
        for corr, rc in zip(correct, rev_correct):
            if hamming(item, corr) == 1:
                corrected[item] = corr
            elif hamming(item, rc) == 1:
                corrected[item] = rc
    return corrected


if __name__ == "__main__":
    file = "/Users/Fiona/Downloads/rosalind_ba1h_475_1_dataset (2).txt";
    strands = read_fasta_dict(file)
    reads = [value for value in strands.values()]
    corrected = correct_reads(reads)
    for key, value in corrected.items():
        print("%s->%s" %(key, value))

