def splicer(s, a, b, c, d):
    output = "%s %s" %(s[a:b + 1], s[c:d + 1])
    return output


if __name__ == "__main__":
    file = input("File path: ")
    with open(file) as input:
        s = input.readline().strip()
        values = input.readline().strip().split(" ")
    a = int(values[0])
    b = int(values[1])
    c = int(values[2])
    d = int(values[3])

    print(splicer(s, a, b, c, d))


