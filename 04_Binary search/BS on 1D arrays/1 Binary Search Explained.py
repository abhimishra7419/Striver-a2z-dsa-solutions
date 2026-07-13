'''MY approach'''
# class Solution:
#     def Binary_search(self, arr, target):
#         n = len(arr)
#         for i in range(n):
#             if arr[i] == target:
#                 return i
# arr = [3, 4, 6, 7, 9, 12, 16, 17]
# target = 6
# a = Solution()
# print(a.Binary_search(arr, target))



'''Better approach or "Iterative Implementation" '''
# class Solution:
#     def Binary_search(self, arr, target):
#         low = 0
#         high = len(arr) - 1
#         while low <= high:
#             mid = (low + high)//2
#             if arr[mid] == target:
#                 return mid
#             elif target > arr[mid]:
#                 low = mid+1
#             else:
#                 high = mid - 1
#         return -1
# arr = [3, 4, 6, 7, 9, 12, 16, 17]
# target = 6
# a = Solution()
# print(a.Binary_search(arr, target))


'''MY Recursive Approach '''
class Solution:
    def Binary_search(self, arr, low, high, target):
        mid = (low + high)//2
        if low > high:
            return -1
        elif arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
            return self.Binary_search(arr, low, high, target)
        else:
            high = mid - 1
            return self.Binary_search(arr, low, high, target)
arr = [3, 4, 6, 7, 9, 12, 16, 17]
target = 6
a = Solution()
print(a.Binary_search(arr, 0, len(arr)-1, target))