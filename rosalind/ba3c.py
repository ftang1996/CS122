def overlap(patterns):
    k = len(patterns[0])
    overlaps = {}
    for i in range(len(patterns)):
        for j in range(len(patterns)):
            if i != j and patterns[i][1:k] == patterns[j][0:k-1]:
                if patterns[i] in overlaps:
                    overlaps[patterns[i]].append(patterns[j])
                else:
                    overlaps[patterns[i]] = [patterns[j]]
    return overlaps


if __name__ == "__main__":
    file = input("File path: ")
    with open(file) as input:
        patterns = [line.strip() for line in input.readlines()]
    overlaps = overlap(patterns)
    for key, values in overlaps.items():
        for value in values:
            print(key + " -> " + value);