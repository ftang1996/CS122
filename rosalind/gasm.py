from rosalind.revc import rev_complement
from rosalind.drbu import de_brujin


def assembly(reads):
    # Decrement k until hamiltonian path is found
    for k in range(len(reads[0]), 0, -1):
        if k == 1:
            print("Wrong")
            return False
        all_reads = []
        for read in reads:
            for i in range(len(read) - k + 1):
                all_reads.append(read[i:i + k])
                all_reads.append(rev_complement(read)[i:i + k])
        edges = de_brujin(all_reads, k-1)
        sequence = ""
        l_node = list(edges.keys())[0]
        while edges != {}:
            r_node = edges[l_node].pop()
            # Remove rev comp
            if rev_complement(l_node) in edges:
                edges[rev_complement(l_node)].pop()
            else:
                break
            sequence += r_node[0]
            if len(edges[l_node]) == 0:
                edges.pop(l_node)
                # Remove rev comp
                edges.pop(rev_complement(l_node))
            if r_node in edges:
                l_node = r_node
            else:
                break
        if edges == {}:
            return sequence


if __name__ == "__main__":
    file = input("File path: ")
    with open(file) as input:
        reads = [line.strip() for line in input.readlines()]
    seq = assembly(reads)
    print(seq)
