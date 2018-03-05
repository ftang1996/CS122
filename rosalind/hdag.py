from collections import deque
from rosalind.utilities import read_edge_list


""" Return path through nodes """
def kahn_topsort(graph):
    uniq_node = set(node for edge in graph for node in edge)
    in_degree = {node: 0 for node in uniq_node}
    for edge in graph:
        in_degree[edge[1]] += 1

    q = deque()
    for node in in_degree:
        if in_degree[node] == 0:
            q.appendleft(node)

    order = []
    while(q):
        n = q.pop()
        order.append(n)
        for edge in graph:
            if edge[0] == n:
                in_degree[edge[1]] -= 1
            if in_degree[edge[1]] == 0:
                q.appendleft(edge[1])
                in_degree[edge[1]] = -1

    if len(order) == len(uniq_node):
        return order
    else:
        return []


def is_hamiltonian(graph, path):
    if not path:
        return -1
    for i in range(len(path)-1):
        is_edge = False
        for edge in graph:
            if edge[0] == path[i] and edge[1] == path[i+1]:
                is_edge = True
                break
        if not is_edge:
            return 0
    return 1


if __name__ == "__main__":
    file = input('File path: ')
    graphs = []
    with open(file) as input:
        num_graphs = int(input.readline().strip())
        text = ""
        line = input.readline()
        while line:
            if line == "\n" and text != "":
                vertices, graph = read_edge_list(text.strip())
                graphs.append(graph)
                text = ""
            else:
                text += line
            line = input.readline()
    vertices, graph = read_edge_list(text.strip())
    graphs.append(graph)

    for graph in graphs:
        path = kahn_topsort(graph)
        if is_hamiltonian(graph, path):
            str = "1 "
            for i in range(len(path)):
                str += path[i] + " "
            print(str)
        else:
            print(-1)