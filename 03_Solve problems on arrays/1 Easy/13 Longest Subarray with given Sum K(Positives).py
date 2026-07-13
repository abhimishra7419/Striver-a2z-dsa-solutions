# class Solution:
#     def longest_subarr(self, arr, k):
#         n = len(arr)
#         maxlenth = 0 
#         for startindex in range(n):
#             for endindex in range(startindex, n):
#                 currentsum = 0
#                 for i in range(startindex, endindex + 1):
#                     currentsum += arr[i]
#                 if currentsum == k:
#                     maxlenth = max(maxlenth, endindex - startindex + 1)
#         return maxlenth
# arr = [1, 3, 4, 5, 5, 4, 9, 0]
# a = Solution()
# print(a.longest_subarr(arr, 10))




'''Optimal appr0cah ↓'''
class Solution:
    def longest_subarr(self, arr, k):
        n = len(arr)
        maxLen = 0
        left = 0
        right = 0
        sum = arr[0]

        while right < n:
            while left <= right and sum > k:
                sum -= arr[left]
                left += 1
            if sum == k:
                maxLen = max(maxLen, right - left + 1)
            
            right += 1
            if right < n:
                sum += arr[right]
        return maxLen
arr = [1, 3, 4, 2, 5, 4, 9, 0]
a = Solution()
print(a.longest_subarr(arr, 10))