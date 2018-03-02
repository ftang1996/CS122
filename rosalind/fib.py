def fib_rabbits(n, k):
    fib = [1, 1];
    for i in range(2, n):
        fib.append(fib[i-1] + k * fib[i-2]);
    return fib[-1];


if __name__ == "__main__":
    file = input("File path: ")
    with open(file) as input:
        values = input.read().strip()
    n = values[0]
    k = values[1]
    print(fib_rabbits(n, k))