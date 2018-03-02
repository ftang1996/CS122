def even_lines(file):
    with open(file) as input:
        output = open("output.txt", 'w')
        odd_line = input.readline()
        while(odd_line):
            even_line = input.readline()
            output.write(even_line)
            odd_line = input.readline()
        output.close()


if __name__ == "__main__":
    file = input("File path: ")
    even_lines(file)