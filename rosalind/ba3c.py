def overlap(patterns):
    k = len(patterns[0])
    prefix = [pattern[0:k-1] for pattern in patterns]
    suffix = [pattern[1:k] for pattern in patterns]
    overlaps = {}
    for i in range(len(patterns)):
        for j in range(len(patterns)):
            if i != j and suffix[i] == prefix[j]:
                overlaps[patterns[i]] = patterns[j]
    return overlaps


if __name__ == "__main__":
    file = input("File path: ")
    with open(file) as input:
        patterns = [line.strip() for line in input.readlines()]
    overlaps = overlap(patterns)
    for key, value in overlaps.items():
        print(key + " -> " + value);