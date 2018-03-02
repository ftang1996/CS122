def hamming(s, t):
    dh = 0
    assert len(s) == len(t), "Strings must be of equal length"
    if s == t:
        return dh
    for i in range(0, len(s)):
        if s[i] != t[i]:
            dh += 1
    return dh


if __name__ == "__main__":
    file = input("File path: ")
    with open(file) as input:
        strings = input.readlines()
    s = strings[0].strip()
    t = strings[1].strip()
    print(hamming(s, t))