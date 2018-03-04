def min_skew(genome):
    # Calculate skews
    skew = [0]
    for i in range(0, len(genome)):
        if genome[i] == "C":
            skew.append(skew[i] - 1)
        elif genome[i] == "G":
            skew.append(skew[i] + 1)
        else:
            skew.append(skew[i])

    # Find min skews
    min_skews = []
    minimum = min(skew)
    for j in range(1, len(skew)):
        if skew[j] == minimum:
            min_skews.append(j)
    return min_skews


if __name__ == "__main__":
    genome = input("Genome Sequence: ")
    min_skews = min_skew(genome)
    for skew in min_skews:
        print(skew)




