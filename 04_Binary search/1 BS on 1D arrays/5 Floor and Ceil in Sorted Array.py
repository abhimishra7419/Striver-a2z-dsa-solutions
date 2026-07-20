'''My brute force'''
# class Solution:
#     def finding_floorandceil(self, arr, x):
#         n = len(arr)
#         if x < arr[0]:
#             return -1, arr[0]
#         for i in range(n):
#             if arr[i] == x:
#                 return arr[i], arr[i]
#             if arr[i] > x:
#                 return arr[i-1], arr[i]
#         if arr[n-1] < x:
#             return arr[n-1], -1
# arr = [3]
# x = 10
# a = Solution()
# print(a.finding_floorandceil(arr, x))


'''My Optimal approach'''
# class Solution:
#     def finding_floorandceil(self, arr, x):
#         n = len(arr)
#         low = 0
#         high = len(arr) - 1
#         ceil = high
#         if arr[0] > x:
#             return -1, arr[0]
#         while low <= high:
#             mid = (low + high)//2
#             if arr[mid] == x:
#                 return arr[mid], arr[mid]
#             elif arr[mid] > x:
#                 ceil = mid
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         if ceil == n-1:
#             return arr[n-1], -1
#         return arr[ceil-1], arr[ceil]
# arr = [3]
# x = 3
# a = Solution()
# print(a.finding_floorandceil(arr, x))



'''Optimal approach'''

class FloorCeilFinder:
    def find_floor(self, arr, x):
        low, high = 0, len(arr) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] <= x:
                ans = arr[mid]
                low = mid + 1
            else:
                high = mid - 1
        return ans

    def find_ceil(self, arr, x):
        low, high = 0, len(arr) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= x:
                ans = arr[mid]
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def get_floor_and_ceil(self, arr, x):
        floor = self.find_floor(arr, x)
        ceil = self.find_ceil(arr, x)
        return floor, ceil
arr = [3, 4, 4, 7, 8, 10]
x = 5
finder = FloorCeilFinder()
f, c = finder.get_floor_and_ceil(arr, x)
print(f"The floor and ceil are: {f} {c}")
