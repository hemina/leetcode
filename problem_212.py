"""
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.



Example:

Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]


Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.

https://leetcode.com/problems/word-search-ii/

@author Mina HE
"""


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return []
        trie = dict()
        result = set()

        for word in words:
            t = trie
            for char in word:
                t = t.setdefault(char, {})  # build word dictionary with "-" to mark the end of a word
            t["-"] = True

        nb_row = len(board)
        nb_col = len(board[0])

        def dfs(t, row, col, path, result):
            if 0 <= row < nb_row and 0 <= col < nb_col:
                char = board[row][col]
                t = t.get(char)
                if not t:
                    return
                if t.get("-"):
                    result.add(path + char)
                board[row][col] = "*"  # set current value as a non-letter to avoid visiting back
                dfs(t, row + 1, col, path + char, result)
                dfs(t, row - 1, col, path + char, result)
                dfs(t, row, col + 1, path + char, result)
                dfs(t, row, col - 1, path + char, result)
                board[row][col] = char  # set current value to its original value for loop of the next starting point

        for row in range(nb_row):
            for col in range(nb_col):
                dfs(trie, row, col, "", result)  # test every starting point of word [row, col]

        return list(result)


"""
Runtime: 296 ms, faster than 84.33% of Python online submissions.
Memory Usage: 28.1 MB, less than 80.07% of Python online submissions.
"""
