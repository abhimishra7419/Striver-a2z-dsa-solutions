'''My brute force'''
# class Solution:
#     def find_upper(self, arr, x):
#         n = len(arr)
#         for i in range(n):
#             if arr[i] > x:
#                 return i
#         return -1
# arr = [1,2,2,3]
# x = 2
# a = Solution()
# print(a.find_upper(arr, x))

'''My Optimal approach'''
class Solution:
    def find_upper(self, arr, x):
        low = 0
        high = len(arr)-1
        ans = -1
        while low <= high:
            mid = (low + high)//2
            if arr[mid] > x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
arr = [1,2,2,3]
x = 2
a = Solution()
print(a.find_upper(arr, x))