'''My brute force'''
# class Solution:
#     def find_peak(self, arr):
#         n = len(arr)
#         ans = n - 1
#         if n == 1:
#             return 0
#         if arr[0] > arr[1]:
#             return 0
#         for i in range(1, n-1):
#             if arr[i] > arr[i-1]:
#                 if arr[i] > arr[i+1]:
#                     ans = i
#         return ans
# arr = [1]
# a = Solution()
# print(a.find_peak(arr))


'''My optimla approach'''
# class Solution:
#     def find_peak(self, arr):
#         n = len(arr)
#         if n == 1:
#             return 0
#         if arr[0] > arr[1]:
#             return 0
#         low, high = 1, n - 2
#         while low <= high:
#             mid = low + (high-low)//2
#             if arr[mid-1] < arr[mid] > arr[mid + 1]:
#                 return mid
#             if arr[mid] > arr[mid-1]:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         if arr[n-1] > arr[n-2]:
#             return n-1
#         return -1
# arr = [1,2,1,3,5,6,4]
# arr1 = [1]
# a = Solution()
# print(a.find_peak(arr))


'''Optimal approach'''
class Solution:
    def findPeakElement(self, nums):
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[mid + 1]:
                high = mid
            else:
                low = mid + 1
        return low
nums = [1]
obj = Solution()
print(obj.findPeakElement(nums))
