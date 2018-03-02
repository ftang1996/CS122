def count_words(s):
    count = dict()
    for word in s.split(" "):
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count


if __name__ == "__main__":
    file = input("File path: ")
    with open(file) as input:
        string = input.read().strip()
    count = count_words(string)
    for key, value in count.items():
        print("%s %s" %(key, value))
