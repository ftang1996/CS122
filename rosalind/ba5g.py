import numpy as np

def edit_distance(s, t):
    m = len(s)
    n = len(t)
    edits = np.zeros((m+1, n+1), dtype=int)
    for y in range(m + 1):
        edits[y][0] = y
    for x in range(n + 1):
        edits[0][x] = x

    for y in range(1, m + 1):
        for x in range(1, n + 1):
            if s[y-1] == t[x-1]:
                d = edits[y-1][x-1]
            else:
                d = edits[y-1][x-1] + 1
            h = edits[y][x-1] + 1
            v = edits[y-1][x] + 1
            edits[y][x] = min(d, h, v)
    return edits[m][n]

if __name__ == "__main__":
    file = input("File path: ")
    with open(file) as input:
        s = input.readline().strip()
        t = input.readline().strip()
    print(edit_distance(s, t))

