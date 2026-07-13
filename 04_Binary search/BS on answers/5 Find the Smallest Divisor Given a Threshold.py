'''My Brute force'''
# import math
# class Solution:
#     def findingdivisor(self, arr, divisor, limit):
#         totalsum = 0
#         for num in arr:
#             totalsum += math.ceil(num/divisor)
#         return totalsum <= limit
        
#     def smallDivisor(self, arr, limit):
#         low = 1
#         high = max(arr)
#         for i in range(1, high+1):
#             if self.findingdivisor(arr, i, limit):
#                 return i
#         return -1
# arr = [100, 100]
# limit = 2
# a = Solution()
# print(a.smallDivisor(arr, limit))


'''My Optimal approach'''
import math
class Solution:
    def findingDivisor(self, arr, mid, limit):
        totalsum = 0
        for num in arr:
            totalsum += math.ceil(num/mid)
        return totalsum <= limit
    def smallDivisor(self, arr, limit):
        low = 1
        high = max(arr)
        ans = -1
        while low <= high:
            mid = (low + high)//2
            if self.findingDivisor(arr, mid, limit):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
arr = [44,22,33,11,1]
limit = 5
a = Solution()
print(a.smallDivisor(arr, limit))
