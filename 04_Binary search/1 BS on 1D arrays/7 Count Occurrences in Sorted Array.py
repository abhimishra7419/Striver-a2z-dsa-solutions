'''My brute force'''
# class Solution:
#     def Counting_occurrences(self, arr, target):
#         n = len(arr)
#         count = 0
#         for i in range(n):
#             if arr[i] == target:
#                 count += 1
#         return count
# arr = [2, 2 , 3 , 3 , 3 , 3 , 4]
# x = 3
# a = Solution()
# print(a.Counting_occurrences(arr, x))

'''My Optimal Solution'''
class Solution:
    def firstseen(self, arr, target):
        low = 0
        high = len(arr) - 1
        first_seen = -1
        while low <= high:
            mid = (low + high)//2
            if arr[mid] == target:
                first_seen = mid
                high = mid - 1
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return first_seen
    def lastseen(self, arr, target):
        low = 0
        high = len(arr) - 1
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
    def counting_occurrences(self, arr, target):
        first_seen = self.firstseen(arr, target)
        last_seen = self.lastseen(arr, target)
        count = last_seen - first_seen + 1
        return count
arr = [2, 2 , 3 , 3 , 3 , 3 , 4]
x = 3
a = Solution()
print(a.counting_occurrences(arr, x))
