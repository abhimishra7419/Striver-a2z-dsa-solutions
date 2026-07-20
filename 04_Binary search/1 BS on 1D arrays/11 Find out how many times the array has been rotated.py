'''My Brute force'''
# class Solution:
#     def findingin(self, arr):
#         n = len(arr)
#         for i in range(n-1):
#             if arr[i] > arr[i+1]:
#                 return i+1
#         return 0
# arr = [3,4,5,6,7,8,1,2]
# a = Solution()
# print(a.findingin(arr))


'''Optimal approach'''
class Solution:
    def findingin(self, arr):
        low = 0
        high = len(arr)-1
        while low < high:
            mid = low + (high - low)//2
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid
        return low
arr = [7,8,9,1,2]
a = Solution()
print(a.findingin(arr))