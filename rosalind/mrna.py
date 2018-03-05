def possible_RNA(protein):
    codon_freq = {
        'I': 3, 'M': 1, 'T': 4, 'N': 2,
        'K': 2, 'S': 6, 'R': 6, 'L': 6,
        'P': 4, 'H': 2, 'Q': 2, 'V': 4,
        'A': 4, 'D': 2, 'E': 2, 'G': 4,
        'F': 2, 'Y': 2, 'C': 2, 'W': 1,
        '_': 3
    }
    protein += '_'
    pRNA = 1
    for i in protein:
        pRNA *= codon_freq[i]
    return pRNA


if __name__ == "__main__":
    file = input("File path: ")
    with open(file) as input:
        protein = input.readline().strip()
    print(possible_RNA(protein))
