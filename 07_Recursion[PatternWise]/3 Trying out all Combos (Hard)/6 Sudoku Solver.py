'''My Solution'''
# class Solution:
#     def solveSudoku(self, board):
#         elements = [str(i) for i in range(1, 10)]
#         def is_safe(k, row, col):
#             for i in range(9):
#                 if board[i][col] == k:
#                     return False
#             for j in range(9):
#                 if board[row][j] == k:
#                     return False
#             box_row = (row // 3) * 3
#             box_col = (col // 3) * 3
#             for i in range(box_row, box_row + 3):
#                 for j in range(box_col, box_col + 3):
#                     if board[i][j] == k:
#                         return False
#             return True
#         def solve():
#             for i in range(9):
#                 for j in range(9):
#                     if board[i][j] == ".":
#                         for k in elements:
#                             if is_safe(k, i, j):
#                                 board[i][j] = k
#                                 if solve():
#                                     return True
#                                 board[i][j] = "."
#                         return False
#             return True

#         solve()

# if __name__ == "__main__":
#     board =  [ ["5", "3", ".", ".", "7", ".", ".", ".", "."] ,
#               ["6", ".", ".", "1", "9", "5", ".", ".", "."] ,
#               [".", "9", "8", ".", ".", ".", ".", "6", "."] ,
#               ["8", ".", ".", ".", "6", ".", ".", ".", "3"] , 
#               ["4", ".", ".", "8", ".", "3", ".", ".", "1"] ,
#               ["7", ".", ".", ".", "2", ".", ".", ".", "6"] ,
#               [".", "6", ".", ".", ".", ".", "2", "8", "."] ,
#               [".", ".", ".", "4", "1", "9", ".", ".", "5"] ,
#               [".", ".", ".", ".", "8", ".", ".", "7", "9"] ]
#     Solution().solveSudoku(board)
#     print(board)

'''Optimal Solution'''

class Solution:
    def solveSudoku(self, board):
        digits = "123456789"

        def candidates(row, col):
            used = set(board[row])
            used.update(board[r][col] for r in range(9))
            br = (row // 3) * 3
            bc = (col // 3) * 3
            for r in range(br, br + 3):
                for c in range(bc, bc + 3):
                    used.add(board[r][c])
            return [d for d in digits if d not in used]
        
        def solve():
            best_cell = None
            best_options = None
            for r in range(9):
                for c in range(9):
                    if board[r][c] != ".":
                        continue
                    options = candidates(r, c)
                    if len(options) == 0:
                        return False
                    if best_options is None or len(options) < len(best_options):
                        best_cell = (r, c)
                        best_options = options
                        if len(options) == 1:
                            break
                if best_options is not None and len(best_options) == 1:
                    break
            if best_cell is None:
                return True
            r, c = best_cell
            for digit in best_options:
                board[r][c] = digit
                if solve():
                    return True
                board[r][c] = "."
            return False
        
        solve()
if __name__ == "__main__":
    board =  [ ["5", "3", ".", ".", "7", ".", ".", ".", "."] ,
              ["6", ".", ".", "1", "9", "5", ".", ".", "."] ,
              [".", "9", "8", ".", ".", ".", ".", "6", "."] ,
              ["8", ".", ".", ".", "6", ".", ".", ".", "3"] , 
              ["4", ".", ".", "8", ".", "3", ".", ".", "1"] ,
              ["7", ".", ".", ".", "2", ".", ".", ".", "6"] ,
              [".", "6", ".", ".", ".", ".", "2", "8", "."] ,
              [".", ".", ".", "4", "1", "9", ".", ".", "5"] ,
              [".", ".", ".", ".", "8", ".", ".", "7", "9"] ]
    Solution().solveSudoku(board)
    print(board)