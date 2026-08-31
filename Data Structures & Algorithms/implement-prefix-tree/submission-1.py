class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode()
            root = root.children[char]
        root.word = True

    def search(self, word: str) -> bool:
        root = self.root
        for char in word:
            if char not in root.children:
                return False
            root = root.children[char]
        return root.word
        

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for char in prefix:
            if char not in root.children:
                return False
            root = root.children[char]
        return True
        
        