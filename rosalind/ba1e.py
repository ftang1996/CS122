""" Return nucleotide for a number """
def to_nucleotide(number):
    symbols = {0: "A", 1: "C", 2: "G", 3: "T"}
    return symbols[number]


""" Return nucleotide pattern for a numeric code"""
def to_pattern(code, k):
    if k == 1:
        return to_nucleotide(code)
    pre_index = code // 4
    remainder = code % 4
    symbol = to_nucleotide(remainder)
    pre_pattern = to_pattern(pre_index, k - 1)
    return pre_pattern + symbol


""" Return number for a nucleotide """
def nucleotide_number(nucleotide):
    numbers = {"A": 0, "C": 1, "G": 2, "T": 3}
    return numbers[nucleotide]


"""Return number code for a nucleotide pattern"""
def pattern_code(pattern):
    if (pattern == ""):
        return 0;
    symbol = pattern[-1];
    prefix = pattern[0:len(pattern)-1];
    return 4 * pattern_code(prefix) + nucleotide_number(symbol);


def compute_freq(text, k):
    frequencies = [];
    for i in range(0, 4**k):
        frequencies.append(0)
    for j in range(0, len(text) - k + 1):
        pattern = text[j:j+k]
        l = pattern_code(pattern)
        frequencies[l] += 1
    return frequencies


def clump_find(genome, k, L, t):
    freq_patterns = []
    clump = []

    # Initialize clump array
    for i in range(0, 4**k):
        clump.append(0)
    # Initialize a frequency array for first window of L
    text = genome[0:L]
    frequencies = compute_freq(text, k)

    # Add new clumps
    for j in range(0, 4**k):
        if frequencies[j] >= t:
            clump[j] = 1

    # Update for each shifted window
    for m in range(1, len(genome) - L + 1):
        last_seq = genome[m - 1:m + k - 1]
        new_seq = genome[m + L - k:m + L]
        frequencies[pattern_code(last_seq)] -= 1
        frequencies[pattern_code(new_seq)] += 1
        # Check if there's new clump
        if frequencies[pattern_code(new_seq)] >= t:
            clump[pattern_code(new_seq)] = 1

    # Array of clumps
    for o in range(0, len(clump)):
        if clump[o] == 1:
            freq_patterns.append(to_pattern(o, k))
    return freq_patterns


if __name__ == "__main__":
    file = input("File path: ")
    with open(file) as input:
        genome = input.readline().strip()
        values = input.readline().strip().split()
    k = int(values[0])
    L = int(values[1])
    t = int(values[2])
    patterns = clump_find(genome, k, L, t)
    for pattern in patterns:
        print(pattern)
