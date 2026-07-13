'''My brute force'''
# class Solution:
#     def calculating(self, arr, i):
#         sum = 0
#         dividing = 1
#         for j in range(len(arr)):
#             if sum + arr[j] <= i:
#                 sum += arr[j]
#             else:
#                 dividing += 1
#                 sum = arr[j]
#         return dividing
#     def DividingBoard(self, arr, k):
#         low = max(arr)
#         high = sum(arr)
#         if len(arr) < k:
#             return -1
#         for i in range(low, high + 1):
#             if self.calculating(arr, i) == k:
#                 return i
#         return low
# arr = [5, 5, 5, 5]
# k = 2
# a = Solution()
# print(a.DividingBoard(arr, k))



'''My Optimal approach'''
class Solution:
    def calculating(self, arr, mid):
        sum = 0
        dividing = 1
        for i in range(len(arr)):
            if sum + arr[i] <= mid:
                sum += arr[i]
            else:
                dividing += 1
                sum = arr[i]
        return dividing
    def DividingBoard(self, arr, k):
        low = max(arr)
        high = sum(arr)
        ans = low
        if len(arr) < k:
            return -1
        while low <= high:
            mid = (low + high)//2
            icalculate = self.calculating(arr, mid)
            if icalculate > k:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
        return ans
arr = [10, 20, 30, 40]
k = 2
a = Solution()
print(a.DividingBoard(arr, k))
