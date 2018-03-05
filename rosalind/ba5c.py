import numpy as np

def LCS(s, t):
    m = len(s)
    n = len(t)
    comp = np.zeros((m+1, n+1), dtype=int)
    path = []
    # Path array for minimum differences
    for y in range(m + 1):
        new = []
        for x in range(n + 1):
            if x == 0 and y == 0:
                new.append('-')
            elif x == 0:
                new.append('L')
            elif y == 0:
                new.append('U')
            else:
                new.append('-')
        path.append(new)
    # Comparison matrix between s and t
    for i in range (1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                comp[i][j] = comp[i - 1][j - 1] + 1
                path[i][j] = 'D'
            else:
                if comp[i - 1][j] >= comp[i][j -1]:
                    comp[i][j] = comp[i - 1][j]
                    path[i][j] = 'U'
                else:
                    comp[i][j] = comp[i][j - 1]
                    path[i][j] = 'L'
    # Build longest common substring
    lcs = ""
    while(m != 0 and n != 0):
        if m == 0 and n == 0:
            return lcs
        elif path[m][n] == 'D':
            LCS = s[m-1] + lcs
            m -= 1
            n -= 1
        elif path[m][n] == 'U':
            m -= 1
        elif path[m][n] == 'L':
            n -= 1
    return lcs


if __name__ == "__main__":
    file = input("File path: ")
    with open(file) as input:
        s = input.readline().strip()
        t = input.readline().strip()
    print(LCS(s, t))