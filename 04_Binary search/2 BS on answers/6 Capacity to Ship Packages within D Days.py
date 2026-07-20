'''brute force'''
# class Solution:
#     def capacitycheck(self, arr, capacity):
#         countload = 0
#         day = 1
#         for num in arr:
#             if countload + num > capacity:
#                 day += 1
#                 countload = num
#             else:
#                 countload += num
#         return day
#     def Shippackages(self, arr, days):
#         low = max(arr)
#         high = sum(arr)
#         for i in range(low, high+1):
#             needed = self.capacitycheck(arr, i)
#             if needed <= days:
#                 return i
#         return high
# arr = [1,2,3,4,5,6,7,8,9,10]
# d = 5
# a = Solution()
# print(a.Shippackages(arr, d))


'''My Optimal approach'''
class Solution:
    def capacitycheck(self, arr, capacity):
        countload = 0
        day = 1
        for num in arr:
            if countload + num > capacity:
                day += 1
                countload = num
            else:
                countload += num
        return day
    def Shippackages(self, arr, days):
        low = max(arr)
        high = sum(arr)
        ans = high
        while low <= high:
            mid = (low + high)//2
            needed = self.capacitycheck(arr, mid)
            if needed <= days:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
arr = [1,2,3,4,5,6,7,8,9,10]
d = 5
a = Solution()
print(a.Shippackages(arr, d))