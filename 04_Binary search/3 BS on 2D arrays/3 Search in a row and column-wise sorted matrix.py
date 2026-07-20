'''My brute force'''
# class Solution:
#     def findingElement(self, mat, target):
#         n = len(mat)
#         m = len(mat[0])
#         for i in range(n):
#             for j in range(m):
#                 if mat[i][j] == target:
#                     return f"Found at {i, j}"
#         return "Not Found"
# matrix = [
#         [1, 4, 7, 11, 15],
#         [2, 5, 8, 12, 19],
#         [3, 6, 9, 16, 22],
#         [10, 13, 14, 17, 24],
#         [18, 21, 23, 26, 30]
#     ]
# target = 9
# a = Solution()
# print(a.findingElement(matrix, target))


'''My better approach'''
# class Solution:
#     def findingCol(self, arr, m, target):
#         low, high = 0, m-2
#         while low <= high:
#             mid = (low + high)//2
#             if arr[mid] == target:
#                 return mid
#             elif arr[mid] < target:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         return m-1
#     def findingElement(self, mat, target):
#         n = len(mat)
#         m = len(mat[0])
#         for i in range(n):
#             col = self.findingCol(mat[i], m, target)
#             if mat[i][col] == target:
#                 return f"Found at {i, col}"
#         return "Not Found"
# matrix = [
#         [1, 4, 7, 11, 15],
#         [2, 5, 8, 12, 19],
#         [3, 6, 9, 16, 22],
#         [10, 13, 14, 17, 24],
#         [18, 21, 23, 26, 30]
#     ]
# target = 9
# a = Solution()
# print(a.findingElement(matrix, target))


'''My Optimal approach'''
class Solution:
    def findingElement(self, mat, target):
        n = len(mat)
        m = len(mat[0])
        row = 0
        col = m-1
        while row < n and col >= 0:
            current = mat[row][col]
            if current == target:
                return f"Found at {row, col}"
            elif current < target:
                row += 1
            else:
                col -= 1
        return "Not found"
matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
matrix1 = [[-5]]
target = 9
a = Solution()
print(a.findingElement(matrix, target))
print(a.findingElement(matrix1, -5))