def nxx(xx, dna):
    lengths = sorted([len(s) for s in dna], reverse=True)
    total = sum(lengths)
    bp = 0
    for l in lengths:
        bp += l
        coverage = bp/total
        if coverage >= xx/100:
            return l


if __name__ == "__main__":
    file = input("File path: ")
    with open(file) as input:
        dna = [line.strip() for line in input.readlines()]
    print(nxx(50, dna))
    print(nxx(75, dna))