import Levenshtein

class BKTreeNode:
    def __init__(self, word):
        self.word = word
        self.children = {}

class BKTree:
    def __init__(self):
        self.root = None

    def add(self, word):
        if self.root is None:
            self.root = BKTreeNode(word)
            return
        current = self.root
        while True:
            dist = Levenshtein.distance(word, current.word)
            if dist == 0:
                return
            if dist not in current.children:
                current.children[dist] = BKTreeNode(word)
                return
            current = current.children[dist]