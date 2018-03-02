def rev_complement(seq):
    base_pairs = {"A": "T", "C": "G", "G": "C", "T": "A"}
    complement = ""
    for i in range(0, len(seq)):
        complement += base_pairs[seq[i]]
    return complement[::-1]


if __name__ == "__main__":
    file = input("File path: ")
    with open(file) as input:
        seq = input.read().strip()
    print(rev_complement(seq))
