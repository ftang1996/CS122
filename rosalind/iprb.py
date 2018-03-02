def p_dominant(k, m, n):
    pop = k + m + n;
    dd = (k / pop) * ((k - 1) / (pop - 1))
    hd = (k / pop) * (m / (pop - 1)) + (m / pop) * (k / (pop - 1))
    dr = (k / pop) * (n / (pop - 1)) + (n / pop) * (k / (pop - 1))
    hh = (m / pop) * ((m - 1) / (pop - 1))
    hr = (m / pop) * (n / (pop - 1)) + (n / pop) * (m / (pop - 1))
    dominant = dd + hd + dr + 0.75*hh + 0.5*hr
    return dominant


if __name__ == "__main__":
    k = int(input("Number of homozygous dominant individuals: "))
    m = int(input("Number of heterozygous individuals: "))
    n = int(input("Number of homozygous recessive individuals: "))
    print(p_dominant(k, m, n))