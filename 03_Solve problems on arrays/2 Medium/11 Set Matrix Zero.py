'''Brute force'''
# class Solution:
#     def setmatrix(self, matrix):
#         m = len(matrix)
#         n = len(matrix[0])
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 0:
#                     for col in range(n):    # for mark whole row
#                         if matrix[i][col] != 0:
#                             matrix[i][col] = -1
#                     for row in range(m):  # for mark whole column
#                         if matrix[row][j] != 0:
#                             matrix[row][j] = -1
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == - 1:
#                     matrix[i][j] = 0
#         return matrix
# arr = [[1,1,1],[1,0,1],[1,1,1]]
# a = Solution()
# print(a.setmatrix(arr))

'''MY Approach'''
# class Solution:
#     def setmatrix(self, matrix):
#         m = len(matrix)
#         n = len(matrix[0])
#         row = [0]*m
#         column = [0]*n
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 0:
#                     row[i]= 1
#                     column[j]= 1
#         for i in range(m):
#             for j in range(n):
#                 if row[i] == 1 or column[j] == 1:
#                     matrix[i][j] = 0
#         return matrix
# arr = [[1,1,1],[1,0,1],[1,1,1]]
# a = Solution()
# print(a.setmatrix(arr))

'''Optimal Approach'''
class Solution:
    def setmatrix(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        frist_row_info = False
        frist_col_info = False
        
        for i in range(n):
            if matrix[0][i] == 0:
                frist_row_info = True
        for i in range(m):
            if matrix[i][0] == 0:
                frist_col_info = True
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if frist_row_info:
            for i in range(n):
                matrix[0][i] = 0
        if frist_col_info:
            for i in range(m):
                matrix[i][0] = 0
        return matrix
arr = [[1,1,1],[1,0,1],[1,1,1]]
a = Solution()
print(a.setmatrix(arr))