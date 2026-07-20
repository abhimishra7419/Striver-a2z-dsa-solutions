'''My Brute force'''
# class Solution:
#     def search_element(self, arr, k):
#         n = len(arr)
#         for i in range(n):
#             if arr[i] == k:
#                 return True
#         return False
# arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
# k = 3
# a = Solution()
# print(a.search_element(arr, k))


'''My Optimal approach'''
# class Solution:
#     def search_element(self, arr, k):
#         low = 0
#         high = len(arr) - 1
#         while low <= high:
#             mid = (low + high)//2
#             if arr[mid] == k:
#                 return True
#             if arr[low] == arr[mid] == arr[high]:
#                 low += 1
#                 high -= 1
#                 continue
#             if arr[mid] >= arr[low]:
#                 if arr[low] <= k < arr[mid]:
#                     high = mid - 1
#                 else:
#                     low = mid + 1
#             else:
#                 if arr[mid] < k <= arr[high]:
#                     low = mid + 1
#                 else:
#                     high = mid - 1
#         return False
# arr = [3,5,1]
# k = 3
# a = Solution()
# print(a.search_element(arr, k))



class Solution:
    def search(self, arr, target) -> bool:
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high)//2
            if arr[mid] == target:
                return True
            if arr[low] == arr[mid] == arr[high]:
                low += 1
                high -= 1
                continue
            if arr[mid] >= arr[low]:
                if arr[low] <= target < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if arr[mid]< target <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False
arr = [3,5,1]
k = 3
a = Solution()
print(a.search(arr, k))
