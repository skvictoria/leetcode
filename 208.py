class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for elem in word:
            if elem not in curr.children:
                curr.children[elem] = TrieNode()
            curr = curr.children[elem]
        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for elem in word:
            if elem not in curr.children:
                return False
            curr = curr.children[elem]
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for elem in prefix:
            if elem not in curr.children:
                return False
            curr = curr.children[elem]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)