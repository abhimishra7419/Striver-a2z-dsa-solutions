# approach
class Solution:
    def dfs(self, i, j, idx, word, board, rows, cols):
        if idx == len(word):
            return True
        if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != word[idx]:
            return False

        temp = board[i][j]
        board[i][j] = '#'

        found = (self.dfs(i + 1, j, idx + 1, word, board, rows, cols)
                or self.dfs(i - 1, j, idx + 1, word, board, rows, cols)
                or self.dfs(i, j + 1, idx + 1, word, board, rows, cols)
                or self.dfs(i, j - 1, idx + 1, word, board, rows, cols))

        board[i][j] = temp

        return found
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                if self.dfs(i, j, 0, word, board, rows, cols):
                    return True

        return False

if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","E"],["A","D","E","E"]]
    word = "ABCCEE"
    print(Solution().exist(board, word))