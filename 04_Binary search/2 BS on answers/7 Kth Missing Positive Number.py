'''Brute force'''
# class Solution:
#     def missingNo(self, arr, k):
#         for num in arr:
#             if num <= k:
#                 k += 1
#             else:
#                 break
#         return k
# arr =  [4,7,9,10]
# k = 10
# a = Solution()
# print(a.missingNo(arr, k))

'''Optimal approach'''
class Solution:
    def missingNo(self, arr, k):
        low, high = 0, len(arr)-1
        while low <= high:
            mid = (low + high)//2
            missing = arr[mid] - (mid + 1)

            if missing < k:
                low = mid + 1
            else: 
                high = mid - 1
        return k + high + 1
arr =  [4,7,9,10]
k = 8
a = Solution()
print(a.missingNo(arr, k))
