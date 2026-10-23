"""
Word Search II
Hard

Given a 2-D grid of characters board and a list of strings words, return all words that are present in the grid.

For a word to be present it must be possible to form the word with a path in the board with horizontally or vertically neighboring cells. The same cell may not be used more than once in a word.

Example 1:
Input:
board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
],
words = ["bat","cat","back","backend","stack"]
Output: ["cat","back","backend"]

Example 2:
Input:
board = [
  ["x","o"],
  ["x","o"]
],
words = ["xoxo"]
Output: []

Constraints:
1 <= board.length, board[i].length <= 12
board[i] consists only of lowercase English letter.
1 <= words.length <= 30,000
1 <= words[i].length <= 10
words[i] consists only of lowercase English letters.
All strings within words are distinct.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None   # full word if a word ends here

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = w

        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(r, c, parent):
            ch = board[r][c]
            node = parent.children[ch]

            if node.word:
                res.append(node.word)
                node.word = None          # avoid duplicates

            board[r][c] = '#'             # mark visited
            for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS
                        and board[nr][nc] in node.children):
                    dfs(nr, nc, node)
            board[r][c] = ch              # backtrack

            # prune: remove exhausted leaf so we never walk it again
            if not node.children:
                del parent.children[ch]

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    dfs(r, c, root)

        return res

if __name__ == "__main__":
    sol = Solution()

    board1 = [
        ["a", "b", "c", "d"],
        ["s", "a", "a", "t"],
        ["a", "c", "k", "e"],
        ["a", "c", "d", "n"],
    ]
    words1 = ["bat", "cat", "back", "backend", "stack"]
    print(sol.findWords(board1, words1))  # expect ['cat', 'back', 'backend'] (any order)

    board2 = [["x", "o"], ["x", "o"]]
    words2 = ["xoxo"]
    print(sol.findWords(board2, words2))  # expect []