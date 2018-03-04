def pattern_match(pattern, string, mismatches):
    matches = []
    for i in range(0, len(string) - len(pattern) + 1):
        window = string[i:i + len(pattern)]
        mismatch = 0
        for j in range(0, len(window)):
            if window[j] != pattern[j]:
                mismatch += 1

        if (mismatch <= mismatches):
            matches.append(i)
    return matches


if __name__ == "__main__":
    file = input("File path: ")
    with open(file) as input:
        pattern = input.readline().strip()
        string = input.readline().strip()
        mismatches = int(input.readline())
    matches = pattern_match(pattern, string, mismatches)
    for match in matches:
        print(match)