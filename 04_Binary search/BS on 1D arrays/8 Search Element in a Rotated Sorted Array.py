'''My brute force'''
# class Solution:
#     def search_element(self, arr, k):
#         n = len(arr)
#         seen = -1
#         for i in range(n):
#             if arr[i] == k:
#                 seen = i
#         return seen
# arr = [4, 5, 6, 7, 0, 1, 2]
# k = 3
# a = Solution()
# print(a.search_element(arr, k))


'''Optimal Solution'''
class Solution:
    def search_element(self, arr, k):
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high)//2
            if arr[mid] == k:
                return mid
            if arr[mid] >= arr[low]:
                if arr[low] <= k < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if arr[mid] < k <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1               
arr = [4, 5, 6, 7, 8, 9, 0, 1, 2]
k = 0
a = Solution()
print(a.search_element(arr, k))