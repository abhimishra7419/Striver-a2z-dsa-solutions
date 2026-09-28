''' My approach '''
# class Solution:
#     def safe(self, row, col, n, curr):
#         copyrow = row
#         copycol = col
#         while row >= 0 and col >= 0:
#             if curr[row][col] == 'Q':
#                 return False
#             row -= 1
#             col -= 1
#         row = copyrow
#         col = copycol
#         while col >= 0:
#             if curr[row][col] == 'Q':
#                 return False
#             col -= 1

#         col = copycol
#         while (row < n) and (col >= 0):
#             if curr[row][col] == 'Q':
#                 return False
#             row += 1
#             col -= 1
#         return True
    
#     def NQueen(self, curr, row, col, n, res):
#         if col == n:
#             possiblecom = ["".join(row) for row in curr]
#             res.append(list(possiblecom))
#             return
#         if row == n:
#             return
#         self.NQueen(curr, row+1, col, n, res)
#         if self.safe(row, col, n, curr):
#             curr[row][col] = 'Q'
#             self.NQueen(curr, 0, col+1, n, res)
#             curr[row][col] = '.'
        
#     def main(self, n):
#         res = []
#         curr = [['.']*n for _ in range(n)]
#         self.NQueen(curr, 0, 0, n, res)
#         return res
# if __name__ == "__main__":
#     n = 4
#     print(Solution().main(n))


'''Optimal approach'''

class Solution:
    def NQueen(self, curr, row, col, n, res, leftrow, uperdaignal, lowerdaignal):
        if col == n:
            possiblecom = ["".join(row) for row in curr]
            res.append(list(possiblecom))
            return
        if row == n:
            return
        self.NQueen(curr, row+1, col, n, res, leftrow, uperdaignal, lowerdaignal)
        if (leftrow[row] == 0) and (lowerdaignal[row+col] == 0) and (uperdaignal[n-1 + row-col] == 0):
            curr[row][col] = 'Q'
            leftrow[row] = 1
            lowerdaignal[row+col] = 1
            uperdaignal[n-1 + row-col] = 1
            self.NQueen(curr, 0, col+1, n, res, leftrow, uperdaignal, lowerdaignal)
            curr[row][col] = '.'
            leftrow[row] = 0
            lowerdaignal[row+col] = 0
            uperdaignal[n-1 + row-col] = 0
        
    def main(self, n):
        leftrow = [0]*n
        uperdaignal = [0]*(2*n-1)
        lowerdaignal = [0]*(2*n-1)
        res = []
        curr = [['.']*n for _ in range(n)]
        self.NQueen(curr, 0, 0, n, res, leftrow, uperdaignal, lowerdaignal)
        return res
if __name__ == "__main__":
    n = 4
    print(Solution().main(n))