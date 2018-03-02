def count_nucleotides(seq):
    count = {"A":0, "C":0, "G":0, "T":0};
    for i in range(0, len(seq)):
        count[seq[i]] += 1
    return count;


if __name__ == "__main__":
    file = input("File path: ")
    with open(file) as input:
        seq = input.read().strip()
    count = count_nucleotides(seq)
    for value in count.values():
        print(value)
