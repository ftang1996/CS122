""" Return dictionary format of FASTA file"""
def read_fasta(file):
    with open(file, 'r') as fasta:
        dna = dict()
        line = fasta.readline().strip()
        while line:
            if line[0] == ">":
                strand = line[1:]
                dna[strand] = ""
            else:
                dna[strand] += line;
            line = fasta.readline().strip()
    return dna