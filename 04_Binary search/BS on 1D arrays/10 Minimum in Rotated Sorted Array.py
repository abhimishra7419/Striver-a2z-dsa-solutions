'''My brute force'''
# class Solution:
#     def mini_element(self, arr):
#         n = len(arr)
#         ans = float('inf')
#         for i in range(n-1):
#             ans = min(ans, arr[i])
#         return ans
# arr = [4,5,6,7,1,2,3]
# a = Solution()
# print(a.mini_element(arr))

'''My Optimal approach'''
# class Solution:
#     def mini_element(self, arr):
#         low = 0
#         high = len(arr) - 1
#         ans = float('inf')
#         while low <= high:
#             mid = (low + high)//2
#             if arr[low] < arr[high]:
#                 ans = min(ans, arr[low])
#                 break
#             elif arr[mid] <= arr[high]:
#                 high = mid - 1
#                 ans = min(ans, arr[mid])
#             else:
#                 low = mid + 1
#         return ans
# arr = [4,5,6,7,0,1,2]
# a = Solution()
# print(a.mini_element(arr))


'''Optimal solution (My first appraoch i tried but didn't get code)'''
class Solution:
    def mini_element(self, arr):
        low, high = 0, len(arr)-1
        while low < high:
            mid = low + (high-low)//2    # very improtant concept why we are using it.
            if arr[mid] < arr[high]:
                high = mid
            else:
                low = mid + 1
        return arr[low]
arr = [11,13,15,17]
a = Solution()
print(a.mini_element(arr))
