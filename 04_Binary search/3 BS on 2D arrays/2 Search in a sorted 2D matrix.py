'''My brute force'''
# class Solution:
#     def FindingElement(self, mat, target):
#         n = len(mat) # number of rows
#         m = len(mat[0]) # number columns
#         for i in range(n):
#             for j in range(m):
#                 if mat[i][j] == target:
#                     return True
#         return False
# mat = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]
# target = 8
# a = Solution()
# print(a.FindingElement(mat, target))


'''My better Solution-I'''   # This is just better then brute force for large input
# class Solution:
#     def FindingElement(self, mat, target):
#         n = len(mat)
#         m = len(mat[0])
#         for i in range(n):
#             if mat[i][m-1] < target:
#                 continue
#             for j in range(m):
#                 if mat[i][j] == target:
#                     return True
#         return False
# mat = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]
# target = 8
# mat2 = [ [1, 2, 4], [6, 7, 8], [9, 10, 34] ]
# target2 = 78
# a = Solution()
# print(a.FindingElement(mat, target))
# print(a.FindingElement(mat2, target2))



'''My better Solution-II''' # This is more cleaner version. and This is just better then brute force for large input
# class Solution:
#     def FindingElement(self, mat, target):
#         n = len(mat)
#         m = len(mat[0])
#         for i in range(n):
#             if mat[i][m-1] >= target:
#                 for j in range(m):
#                     if mat[i][j] == target:
#                         return True
#         return False
# mat = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]
# target = 8
# mat2 = [ [1, 2, 4], [6, 7, 8], [9, 10, 34] ]
# target2 = 78
# a = Solution()
# print(a.FindingElement(mat, target))
# print(a.FindingElement(mat2, target2))



'''My more better Solution'''
# class Solution:
#     def BSserach(self, arr, m, target):
#         low, high = 0, m-1
#         while low <= high:
#             mid = (low + high)//2
#             if arr[mid] == target:
#                 return True
#             elif arr[mid] > target:
#                 high = mid - 1
#             else:
#                 low = mid + 1
#     def FindingElement(self, mat, target):
#         n = len(mat)
#         m = len(mat[0])
#         for i in range(n):
#             if mat[i][0] <= mat[i][m-1] <= target:
#                 if self.BSserach(mat[i], m, target):
#                     return True
#         return False
# mat = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]
# target = 8
# mat2 = [ [1, 2, 4], [6, 7, 8], [9, 10, 34] ]
# target2 = 78
# a = Solution()
# print(a.FindingElement(mat, target))
# print(a.FindingElement(mat2, target2))


'''My Optimal approach'''
# class Solution:
#     def BSforCol(self, arr, m, target):
#         low, high = 0, m-1
#         while low <= high:
#             mid = (low + high)//2
#             if arr[mid] == target:
#                 return True
#             elif arr[mid] > target:
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         return False
#     def FindingElement(self, mat, target):
#         n = len(mat)
#         m = len(mat[0])
#         low, high = 0, n-1
#         targetrow = -1
#         while low <= high:
#             mid = (low + high)//2
#             if mat[mid][0] <= target <= mat[mid][m-1]:
#                 targetrow = mid
#                 break
#             elif mat[mid][0] > target:
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         if targetrow == -1:
#             return -1
#         if self.BSforCol(mat[mid], m, target):
#             return True
#         return False
# mat = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]
# target = 8
# mat2 = [ [1, 2, 4], [6, 7, 8], [9, 10, 34] ]
# target2 = 78
# a = Solution()
# print(a.FindingElement(mat, target))
# print(a.FindingElement(mat2, target2))


'''Optimal approach'''
class Solution:
    def FindingElement(self, mat, target):
        n = len(mat)
        m = len(mat[0])
        low, high = 0, (m*n)-1
        while low <= high:
            mid = (low + high)//2
            row = mid // m
            col = mid % m
            if mat[row][col] == target:
                return True
            elif mat[row][col] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
mat = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]
target = 8
mat2 = [ [1, 2, 4], [6, 7, 8], [9, 10, 34] ]
target2 = 78
a = Solution()
print(a.FindingElement(mat, target))
print(a.FindingElement(mat2, target2))