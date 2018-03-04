import math


def random_prob(dna, gc_content):
    AT = 0;
    GC = 0;
    for i in range(0, len(dna)):
        if dna[i] == "A" or dna[i] == "T":
            AT += 1
        elif dna[i] == "G" or dna[i] == "C":
            GC += 1
    log_p = []
    for content in gc_content:
        p = math.log10((content / 2) ** GC * ((1 - content) / 2) ** AT)
        log_p.append(p)
    return log_p


if __name__ == "__main__":
    file = input("File path: ")
    with open(file) as input:
        dna = input.readline().strip()
        values = input.readline().strip().split(' ')
    gc_content = [float(value) for value in values]
    log_p = random_prob(dna, gc_content)
    for p in log_p:
        print(p)
