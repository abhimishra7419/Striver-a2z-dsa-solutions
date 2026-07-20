'''My brute force'''
# class Solution:
#     def findingRow(self, arr):
#         n = len(arr)  # no. of rows
#         m = len(arr[0])  # no. of columns
#         MaxRow = 0  # to store maximum no. of one in anyrow
#         row = -1   # sotre row index
#         for i in range(n):
#             count = 0
#             for j in range(m):
#                 if arr[i][j] == 1:
#                     count += 1
#             if MaxRow < count:
#                 MaxRow = count
#                 row = i
#         return row
# mat = [[0, 0], [0, 0], [0, 0]]
# a = Solution()
# print(a.findingRow(mat))

'''Optimal apporach'''
class Solution:
    def lower_bound(self, arr, m, x):
        low, high = 0, m-1
        ans = m
        while low <= high:
            mid = (low + high)//2
            if arr[mid] >= x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
    def findingRow(self, arr):
        n = len(arr)
        m = len(arr[0])
        MaxRow = 0
        rowIndex = -1
        for i in range(n):
            countOne = m - self.lower_bound(arr[i], m, 1)
            if countOne > MaxRow:
                MaxRow = countOne
                rowIndex = i
        return rowIndex
mat =  [[1, 1, 1], [0, 0, 1], [0, 0, 0]]
a = Solution()
print(a.findingRow(mat))