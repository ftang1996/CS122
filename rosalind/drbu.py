from rosalind.revc import rev_complement


def de_brujin(reads, k):
    # Only unique reads
    reads = set(reads)
    edges = {}
    for read in reads:
        if read[:k] in edges:
            edges[read[:k]].append(read[len(read)-k:])
        else:
            edges[read[:k]] = [read[len(read)-k:]]
    return edges


if __name__ == "__main__":
    file = input("File path: ")
    with open(file) as input:
        data = [line.strip() for line in input.readlines()]
    reads = []
    for read in data:
        reads.append(read)
        reads.append(rev_complement(read))
    edges = de_brujin(reads, 3)
    for key, values in edges.items():
        for value in values:
            print("(%s, %s)" %(key, value))
