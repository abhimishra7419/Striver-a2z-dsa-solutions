'''Brute force'''
# import math
# class Solution:
#     def calculate_totalhours(self, arr, hourly):
#         totalhour = 0
#         for pile in arr:
#             totalhour += math.ceil(pile/hourly)   # math.ceil() it helps in round off number
#         return totalhour
#     def mineatingspeed(self, arr, h):
#         maxval = max(arr)
#         for i in range(1, maxval+1):
#             hour = self.calculate_totalhours(arr, i)
        
#             if hour <= h:
#                 return i
#         return maxval
# arr = [7, 15, 6, 3]
# h = 8
# a = Solution()
# print(a.mineatingspeed(arr, h))


'''My Optimal approach'''
import math
class Solution:
    def calculate_totalhours(self, arr, mid):
        totalhour = 0
        for pile in arr:
            totalhour += math.ceil(pile/mid)
        return totalhour
    def mineatingspeed(self, arr, h):
        low = 1
        high = max(arr)
        ans = max(arr)
        while low <= high:
            mid = (low + high) //2
            hour = self.calculate_totalhours(arr, mid)
            if hour <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
arr = [7, 15, 6, 3]
h = 8
a = Solution()
print(a.mineatingspeed(arr, h))