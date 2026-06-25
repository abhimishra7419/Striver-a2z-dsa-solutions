'''Brute force'''
# class Solution:
#     def binary_serach(self, arr, num):
#         n = len(arr)
#         for i in range(n):
#             if num == arr[i]:
#                 return True
#         return False
#     def longest_consecutive(self, arr):
#         n = len(arr)
#         longest_con = 1
#         for i in range(len(arr)):
#             x = arr[i]
#             count = 1
#             while self.binary_serach(arr, x+1):
#                 x += 1
#                 count += 1
#             longest_con = max(longest_con, count)
#         return longest_con
# arr = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1, 10, 11, 12]
# a = Solution()
# print(a.longest_consecutive(arr))

# '''Better Approach'''
# class Solution:
#     def longest_consecutive(self, arr):
#         arr.sort()
#         n = len(arr)
#         last_smaller = float('-inf')
#         count = 1
#         longest = 1
#         for i in range(n):
#             if arr[i] - 1 == last_smaller:
#                 count += 1
#                 last_smaller = arr[i]
#             elif arr[i] != last_smaller:
#                 count = 1
#                 last_smaller = arr[i]
#             longest = max(longest, count)
#         return longest
# arr = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1, 10, 11, 12]
# a = Solution()
# print(a.longest_consecutive(arr))


'''Optimal Approach'''
class Solution:
    def longest_consecutive(self, arr):
        arr = set(arr)
        longest = 1
        for i in arr:
            if i-1 not in arr:
                count = 1
                x = i
                while x+1 in arr:
                    count += 1
                    x += 1
                longest = max(longest, count)
        return longest
arr = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1, 10, 11, 12]
a = Solution()
print(a.longest_consecutive(arr))