class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Solution:
    def build_trie(self, words):
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end_of_word = True
        return root

    def dfs(self, board, i, j, node, path, visited, result):
        if node.is_end_of_word:
            result.add(path)
        
        visited[i][j] = True
        R, C = len(board), len(board[0])
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if 0 <= ni < R and 0 <= nj < C and not visited[ni][nj]:
                next_char = board[ni][nj]
                if next_char in node.children:
                    self.dfs(board, ni, nj, node.children[next_char], path + next_char, visited, result)
        
        visited[i][j] = False

    def wordBoggle(self, board, dictionary):
        trie = self.build_trie(dictionary)
        R, C = len(board), len(board[0])
        visited = [[False]*C for _ in range(R)]
        result = set()
        
        for i in range(R):
            for j in range(C):
                char = board[i][j]
                if char in trie.children:
                    self.dfs(board, i, j, trie.children[char], char, visited, result)
        
        return sorted(result)

# Example Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    board1 = [['C','A','P'],['A','N','D'],['T','I','E']]
    dict1 = ["CAT"]
    print(sol.wordBoggle(board1, dict1))  # Output: ['CAT']

    board2 = [['G','I','Z'],['U','E','K'],['Q','S','E']]
    dict2 = ["GEEKS","FOR","QUIZ","GO"]
    print(sol.wordBoggle(board2, dict2))  # Output: ['GEEKS', 'QUIZ']

    board3 = [['A','B'],['C','D']]
    dict3 = ["ABCD","ACBD","ADCB"]
    print(sol.wordBoggle(board3, dict3))  # Output: ['ABCD', 'ACBD']
