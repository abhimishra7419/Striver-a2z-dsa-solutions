'''Brute force'''
# class Solution:
#     def subarray(self, arr):
#         n = len(arr)
#         max_lenth = float('-inf')
#         lenth = 0
#         for i in range(n):
#             sum = 0
#             for j in range(i, n):
#                 sum += arr[j]
#                 if sum == 0:
#                     lenth = j - i + 1
#             max_lenth = max(max_lenth, lenth)
#         return max_lenth
# arr = [9, -3, 3, -1, 6, -5]
# a = Solution()
# print(a.subarray(arr))


'''Optimal approach'''
class Solution:
    def subarray(self, arr):
        n = len(arr)
        mpp: dict[int, int] = {}
        max_lenth = 0
        sum = 0
        for i in range(n):
            sum += arr[i]
            if sum == 0:
                max_lenth = i+1
            else:
                if sum in mpp:
                    max_lenth = max(max_lenth, i-mpp[sum])
                else:
                    mpp[sum] = i
        return max_lenth
arr = [9, -3, 3, -1, 6, -5]
a = Solution()
print(a.subarray(arr))
