# User function Template for python3

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.isEnd

    def isPrefix(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True
# Test Case 1
trie = Trie()
queries = [[1, "abcd"], [1, "abc"], [1, "bcd"], [2, "bc"], [3, "bc"], [2, "abc"]]
output = []
for q in queries:
    if q[0] == 1:
        trie.insert(q[1])
    elif q[0] == 2:
        output.append(trie.search(q[1]))
    else:
        output.append(trie.isPrefix(q[1]))
print(output)   # ➜ [False, True, True]

# Test Case 2
trie = Trie()
queries = [[1, "gfg"], [1, "geeks"], [3, "fg"], [3, "geek"], [2, "for"]]
output = []
for q in queries:
    if q[0] == 1:
        trie.insert(q[1])
    elif q[0] == 2:
        output.append(trie.search(q[1]))
    else:
        output.append(trie.isPrefix(q[1]))
print(output)   # ➜ [False, True, False]
