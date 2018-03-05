class Node:
    def __init__(self, char=0):
        self.char = char
        self.children = dict()

    def add_child(self, newNode):
        self.children[newNode.char] = newNode


class Trie:
    def __init__(self):
        self.root = Node()

    def add_word(self, word):
        current = self.root
        prefix = True
        for i in range(0, len(word)):
            new = Node(word[i])
            if prefix:
                if new.char in current.children:
                    current = current.children[new.char]
                    continue
                current.add_child(new)
                current = current.children[new.char]
                prefix = False
            else:
                current.add_child(new)
                current = current.children[new.char]


def prefix_trie_match(text, trie):
    i = 0
    symbol = text[i]
    v = trie.root
    pattern = ""
    while symbol in v.children:
        pattern += symbol
        v = v.children[symbol]
        i += 1
        if i < len(text):
            symbol = text[i]
    if v.children == {}:
        return pattern
    return -1


def trie_matching(patterns, text):
    trie = Trie()
    for pattern in patterns:
        trie.add_word(pattern);
    matches = []
    for i in range(len(text) - len(patterns[0]) + 1):
        pattern = prefix_trie_match(text[i:], trie)
        if pattern != -1:
            matches.append(i)
    return matches


if __name__ == "__main__":
    file = input("File path: ")
    with open(file) as input:
        string = input.readline().strip()
        patterns = []
        line = input.readline().strip()
        while line:
            patterns.append(line)
            line = input.readline().strip()
    matches = trie_matching(patterns, string)
    for i in matches:
        print(i)

