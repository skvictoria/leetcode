class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for elem in word:
            if elem not in curr.children:
                curr.children[elem] = TrieNode()
            curr = curr.children[elem]
        curr.word = True

    def search(self, word: str) -> bool:
        # recursive DFS function
        def dfs(index, root):
            curr = root

            for i in range(index, len(word)):
                char = word[i]
                if char != "." and char not in curr.children:
                    return False
                elif char == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                curr = curr.children[char]
            return curr.word

        return dfs(0, self.root)

        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
