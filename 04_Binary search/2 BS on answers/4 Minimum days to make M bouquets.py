'''Brute force'''
# class Solution:
#     def isposibile(self, arr, day, m, k):
#         bouquests = 0
#         count = 0
#         for bloom in arr:
#             if bloom <= day:
#                 count += 1
#                 if count == k:
#                     bouquests += 1
#                     count = 0
#             else:
#                 count = 0
#         return bouquests >= m
#     def min_day(self, arr, m, k):
#         totalflowers = m*k
#         if totalflowers > len(arr):
#             return -1
#         low = min(arr)
#         high = max(arr)
#         for day in range(low, high+1):
#             if self.isposibile(arr, day, m, k):
#                 return day
#         return -1
# arr = [7, 7, 7, 7, 13, 11, 12, 7]
# m = 2
# k = 3
# a = Solution()
# print(a.min_day(arr, m, k))



'''My Optimal approach'''
class Solution:
    def isposibile(self, arr, day, m, k):
        bouquets = 0
        count = 0
        for bloom in arr:
            if bloom <= day:
                count += 1
                if count == k:
                    bouquets += 1
                    count = 0
            else:
                count = 0
        return bouquets >= m
    def min_day(self, arr, m, k):
        totalflowers = m*k
        ans = -1
        if totalflowers > len(arr):
            return -1
        low = min(arr)
        high = max(arr)
        while low <= high:
            mid = (low + high)//2
            if self.isposibile(arr, mid, m, k):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
arr = [7,7,7,7,12,7,7]
m = 2
k = 3
a = Solution()
print(a.min_day(arr, m, k))



