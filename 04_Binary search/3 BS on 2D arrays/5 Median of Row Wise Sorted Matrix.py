'''My brute force'''
# class Solution:
#     def findingMedian(self, mat):
#         arr = []
#         n = len(mat)
#         m = len(mat[0])
#         for i in range(n):
#             for j in range(m):
#                 arr.append(mat[i][j])
#         arr.sort()
#         N = len(arr)
#         if N % 2 == 0:
#             return (arr[N//2] + arr[N-1//2]), arr
#         else:
#             return (arr[N//2]), arr
# mat = matrix = [
#     [1, 3, 5],
#     [2, 6, 9],
#     [3, 6, 9]
# ]
# a = Solution()
# print(a.findingMedian(mat))



'''Optimal approach'''
import bisect
class Solution:
    def searchspace(self, row, mid):   # returns index that values has just bigger then mid -> (bisect_right(..., .....))
        return bisect.bisect_right(row, mid)  # retuns count of numbers those are <= mid
    
    def findingMedian(self, mat):
        n = len(mat)
        m = len(mat[0])
        low = min(row[0] for row in mat)
        high = max(row[-1] for row in mat)
        while low < high:
            mid = (low + high)//2
            count = 0
            for row in mat:
                count += self.searchspace(row, mid)
            if count < ((n*m)+1)//2:
                low = mid + 1
            else:
                high = mid
        return low
mat = matrix = [
    [1, 3, 5],
    [2, 6, 9],
    [3, 6, 9]
]
a = Solution()
print(a.findingMedian(mat))