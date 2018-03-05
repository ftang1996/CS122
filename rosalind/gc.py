from rosalind.utilities import read_fasta_dict


def gc_content(seq):
    gc = 0
    for i in range(len(seq)):
        if seq[i] == "C" or seq[i] == "G":
            gc += 1
    return gc/len(seq) * 100


def max_gc(strands):
    gc_contents = dict()
    for strand, seq in strands.items():
        gc_contents[strand] = gc_content(seq)
    max_strand = max(gc_contents, key=gc_contents.get)
    return max_strand, gc_contents[max_strand]


if __name__ == "__main__":
    file = input("File path: ")
    strands = read_fasta_dict(file)
    max_strand, content = max_gc(strands)
    print("%s\n%f" %(max_strand, content))