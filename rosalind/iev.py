def dom_offspring(AAAA, AAAa, AAaa, AaAa, Aaaa, aaaa):
    p_AAAA = 1
    p_AAAa = 1
    p_AAaa = 1
    p_AaAa = .75
    p_Aaaa = .5
    p_aaaa = 0

    dominant = (2 * p_AAAA * AAAA) + (2 * p_AAAa * AAAa) + (2 * p_AAaa * AAaa) + (2 * p_AaAa * AaAa) + (
            2 * p_Aaaa * Aaaa) + (2 * p_aaaa * aaaa)
    return dominant


if __name__ == "__main__":
    file = input("File path: ")
    with open(file) as input:
        values = input.readline().strip().split()
    AAAA = int(values[0])
    AAAa = int(values[1])
    AAaa = int(values[2])
    AaAa = int(values[3])
    Aaaa = int(values[4])
    aaaa = int(values[5])
    print(dom_offspring(AAAA, AAAa, AAaa, AaAa, Aaaa, aaaa))




