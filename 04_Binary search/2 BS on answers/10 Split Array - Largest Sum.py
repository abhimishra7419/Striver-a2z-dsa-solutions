'''My Brute force'''
# class Solution:
#     def findinglargest(self, arr, i):
#         sum = 0
#         splited = 1
#         for j in range(len(arr)):
#             if sum + arr[j] <= i:
#                 sum += arr[j]
#             else:
#                 splited += 1
#                 sum = arr[j]
#         return splited
#     def split(self, arr, k):
#         low = max(arr)
#         high = sum(arr)
#         if len(arr) < k:
#             return -1
#         for i in range(low, high+1):
#             if self.findinglargest(arr, i) == k:
#                 return i
#         return low
# arr = [3,5,1]
# k = 3
# a = Solution()
# print(a.split(arr, k))

'''My Optimal approach'''
class Solution:
    def findinglargest(self, arr, mid):
        sum = 0
        splited = 1
        for i in range(len(arr)):
            if sum + arr[i] <= mid:
                sum += arr[i]
            else:
                splited += 1
                sum = arr[i]
        return splited
    def split(self, arr, k):
        low = max(arr)
        high = sum(arr)
        ans = max(arr)
        if len(arr) < k:
            return -1
        while low <= high:
            mid = (low + high)//2
            icalcualte = self.findinglargest(arr, mid)
            if icalcualte > k:
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
        return ans
arr = [1,2,3,4,5]
k = 4
a = Solution()
print(a.split(arr, k))