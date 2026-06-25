# '''Brute force'''
# class Solution:
#     def maximum_subarray(self, arr):
#         n = len(arr)
#         max_sum = float('-inf')
#         for i in range(n):
#             for j in range(i, n):
#                 sum = 0
#                 for r in range(i, j+1):
#                     sum += arr[r]
#                     max_sum = max(max_sum, sum)
#         return max_sum
# arr = [-2, -3, -7, -2, -10, -4]
# a = Solution()
# print(a.maximum_subarray(arr))

'''Better approach'''
# class Solution:
#     def maximum_subarray(self, arr):
#         n = len(arr)
#         max_sum = float('-inf')
#         for i in range(n):
#             sum = 0
#             for j in range(i, n):
#                 sum += arr[j]
#                 max_sum = max(max_sum, sum)
#         return max_sum
# arr = [-2, -3, -7, -2, -10, -4]
# arr2 = [2, 3, 5, -2, 7, -4]
# a = Solution()
# print(a.maximum_subarray(arr))
# print(a.maximum_subarray(arr2))



'''Optimal approach'''
class Solution:
    def maximum_subarray(self, arr):
        n = len(arr)
        max_sum = float('-inf')
        sum = 0
        for i in range(n):
            sum += arr[i]
            if sum > max_sum:
                max_sum = sum
            if sum < 0:
                sum = 0
        return max_sum
arr = [2, 3, -7, 4, 7, -4]
arr2 = [2, 3, 5, -2, 7, -4]
arr3 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
a = Solution()
print(a.maximum_subarray(arr))
print(a.maximum_subarray(arr2))
print(a.maximum_subarray(arr3))