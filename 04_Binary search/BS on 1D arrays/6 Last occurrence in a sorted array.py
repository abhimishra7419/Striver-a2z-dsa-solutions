'''My brute force'''
# class Solution:
#     def last_occurrence(self, arr, target):
#         n = len(arr)
#         last_seen = -1
#         for i in range(n):
#             if arr[i] == target:
#                 last_seen = i
#         return last_seen
# arr = [3, 4, 13, 13, 13, 20, 40]
# x = 60
# a = Solution()
# print(a.last_occurrence(arr, x))


'''My Optimal approach'''
# class Solution:
#     def last_occurrence(self, arr, target):
#         low = 0
#         high = len(arr)-1
#         last_seen = -1
#         while low <= high:
#             mid = (low + high)//2
#             if arr[mid] == target:
#                 last_seen = mid
#             if arr[mid] <= target:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         return last_seen
# arr = [3, 4, 13, 13, 13, 20, 40]
# x = 13
# a = Solution()
# print(a.last_occurrence(arr, x))





'''My Optimal approach (easy to read)'''
# class Solution:
#     def last_occurrence(self, arr, target):
#         low = 0
#         high = len(arr)-1
#         last_seen = -1
#         while low <= high:
#             mid = (low + high)//2
#             if arr[mid] == target:
#                 last_seen = mid
#                 low = mid + 1
#             elif arr[mid] < target:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         return last_seen
# arr = [3, 4, 13, 13, 13, 20, 40]
# x = 13
# a = Solution()
# print(a.last_occurrence(arr, x))



'''For leetcode'''
class Solution:
    def firstseen(self, arr, target):
        low = 0
        high = len(arr) - 1
        first_seen = -1
        while low <= high:
            mid = (low + high)//2
            if  arr[mid] == target:
                first_seen = mid
                high = mid - 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return first_seen
    def lastseen(self, arr, target):
        low = 0
        high = len(arr)-1
        last_seen = -1
        while low <= high:
            mid = (low + high)//2
            if arr[mid] == target:
                last_seen = mid
                low = mid + 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return last_seen
    def searchRange(self, arr, target):
        first_seen = self.firstseen(arr, target)
        last_seen = self.lastseen(arr, target)
        return [first_seen, last_seen]
arr = [5,7,7,8,8,10]
x = 8
a = Solution()
print(a.searchRange(arr, x))