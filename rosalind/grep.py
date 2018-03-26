def all_sequences(reads):
    sequences = []
    k = len(reads[0])
    # Record different path routes
    path_queue = [reads[:]]
    start_queue = [reads[0]]
    seq_queue = [""]

    while path_queue != []:
        start_node = start_queue.pop()
        path = path_queue.pop()
        l_node = path.pop(path.index(start_node))
        sequence = seq_queue.pop() + l_node[0]
        while path != []:
            r_node = []
            # Add to path queue if node has multiple edges
            for node in path:
                if l_node != node and l_node[1:] == node[:k-1] and node not in r_node:
                    r_node.append(node)
            if len(r_node) > 1:
                for i in range(1, len(r_node)):
                    path_queue.append(path[:])
                    seq_queue.append(sequence)
                    start_queue.append(r_node[i])
            # If r_node is empty, path is not hamiltonian
            if r_node == []:
                break
            l_node = path.pop(path.index(r_node[0]))
            sequence += l_node[0]
        # Add sequence if path was hamiltonian
        if len(sequence) == len(reads):
            sequences.append(sequence)
    return sequences


if __name__ == "__main__":
    file = "/Users/Fiona/Downloads/rosalind_grep.txt"
    with open(file) as input:
        reads = [line.strip() for line in input.readlines()]
    sequences = all_sequences(reads)
    for sequence in sequences:
        print(sequence)
