from rosalind.drbu import de_brujin


def cyclic_perf(reads):
    edges = de_brujin(reads, len(reads[0]) - 1)
    sequence = ""
    l_node = list(edges.keys())[0]
    while edges != {}:
        r_node = edges[l_node].pop()
        sequence += r_node[0]
        if len(edges[l_node]) == 0:
            edges.pop(l_node)
        if r_node in edges:
            l_node = r_node
    return sequence


if __name__ == "__main__":
    file = input("File path: ")
    file = "/Users/Fiona/Downloads/rosalind_asmq.txt"
    with open(file) as input:
        reads = [line.strip() for line in input.readlines()]
    cyclic = cyclic_perf(reads)
    print(cyclic)

