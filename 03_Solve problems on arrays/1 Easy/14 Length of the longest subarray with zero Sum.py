'''Brute force(by my self)'''
# class Solution:
#     def longest_sub(self, arr, k):
#         n = len(arr)
#         maxlenth = 0
#         for i in range(n):
#             for j in range(i, n):
#                 currentsum = 0
#                 for l in range(i, j+1):
#                     currentsum += arr[l]
#                 if currentsum == k:
#                     maxlenth = max(maxlenth, j+1-i)
#         return maxlenth
# arr = [6, -2, 2, -8, 1, 7, 4, -10]
# a = Solution()
# print(a.longest_sub(arr, 0))

'''Brute force'''
# class Solution:
#     def longest_sub(self, arr, k):
#         n = len(arr)
#         maxlenth = 0
#         for i in range(n):
#             currentsum = 0
#             for j in range(i, n):
#                 currentsum += arr[j]
#                 if currentsum == k:
#                     maxlenth = max(maxlenth, j+1-i)
#         return maxlenth
# arr = [6, -2, 2, -8, 1, 7, 4, -10]
# a = Solution()
# print(a.longest_sub(arr, 0))


# '''Brute force'''
# class Solution:
#     def longest_sub(self, arr):
#         max_len = 0
#         sum_index = {}
#         s = 0
#         for index, value in enumerate(arr):
#             s += value
#             if s == 0:
#                 max_len = index + 1
#             elif s in sum_index:
#                 max_len = max(max_len, index-sum_index[s])
#             else:
#                 sum_index[s] = index
#         return max_len
# arr = [9, -3, 3, -1, 6, -5]
# arr1 = [6, -2, 2, -8, 1, 7, 4, -10]
# a = Solution()
# print(a.longest_sub(arr))
# print(a.longest_sub(arr1))


'''Optimal approach'''
class Solution:
    def longest_sub(self, arr):
        n = len(arr)
        max_len = 0
        mpp : dict[int, int] = {}
        sum = 0
        for i in range(n):
            sum += arr[i]
            if sum == 0:
                max_len = i+1
            else:
                if sum in mpp:
                    max_len = max(max_len, i-mpp[sum])
                else:
                    mpp[sum] = i
        return max_len
arr = [9, -3, 3, -1, 6, -5]
arr1 = [6, 2, 2, -8, 1, 7, 4, -10]
a = Solution()
print(a.longest_sub(arr))
print(a.longest_sub(arr1))