from rosalind.utilities import read_edge_list

def vertex_deg(edges):
    degrees = {}
    for edge in edges:
        for num in edge:
            if num not in degrees:
                degrees[num] = 1
            else:
                degrees[num] += 1
    return degrees


if __name__ == "__main__":
    file = input("File path: ")
    with open(file) as input:
        text = input.read()
    vertices, edges = read_edge_list(text)
    degrees = vertex_deg(edges)

    for i in range(1, vertices + 1):
        print(degrees[str(i)])
