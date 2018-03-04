def probability(kmer, profile):
    p = 1
    for i in range(len(kmer)):
        if kmer[i] == "A":
            p *= profile[0][i]
        elif kmer[i] == "C":
            p *= profile[1][i]
        elif kmer[i] == "G":
            p *= profile[2][i]
        elif kmer[i] == "T":
            p *= profile[3][i]
    return p


def pp_kmer(seq, k, profile):
    kmers = [seq[i:i + k] for i in range(len(seq) - k + 1)]
    p = []
    for i in range(len(kmers)):
        p.append(probability(kmers[i], profile))
    maximum = p.index(max(p))
    return kmers[maximum]


if __name__ == "__main__":
    file = input("File path: ")
    with open(file) as input:
        seq = input.readline().strip()
        k = int(input.readline().strip())
        profile = []
        row = input.readline().strip()
        while row:
            profile.append([float(i) for i in row.split()])
            row = input.readline().strip()
    print(pp_kmer(seq, k, profile))
