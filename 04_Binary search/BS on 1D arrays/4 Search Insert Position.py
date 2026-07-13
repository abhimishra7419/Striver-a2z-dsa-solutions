'''My brute force'''
# class Solution:
#     def insert_position(self, arr, x):
#         n = len(arr)
#         for i in range(n):
#             if x <= arr[i]:
#                 arr.insert(i, x)
#         return arr
# arr = [1,2,4,7]
# x = 6
# a = Solution()
# print(a.insert_position(arr, x))


'''MY Optimal approach'''
class Solution:
    def insert_position(self, arr, x):
        low = 0
        high = len(arr) - 1
        ans = high
        while low <= high:
            mid = (low + high)//2
            if arr[mid] >= x:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        arr.insert(ans, x)
        return arr
arr = [1,2,4,7]
x = 6
a = Solution()
print(a.insert_position(arr, x))