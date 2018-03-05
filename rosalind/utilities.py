""" Return dictionary format of FASTA file"""
def read_fasta_dict(file):
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


""" Return list format of FASTA file"""
def read_fasta_list(file):
    with open(file, 'r') as fasta:
        dna = []
        line = fasta.readline().strip()
        index = -1
        while line:
            if line[0] == ">":
                dna.append("")
                index += 1
            else:
                dna[index] += line
            line = fasta.readline().strip()
    return dna


"""Return number of vertices and list of edges from file in edge list format"""
def read_edge_list(text):
    values = text.split("\n")
    vertices = int(values[0].split(" ")[0])
    edges = [row.split() for row in values[1:]]
    return vertices, edges

