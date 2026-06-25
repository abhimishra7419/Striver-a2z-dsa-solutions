# class Solution:
#     def check(self, arr):
#         n = len(arr)
#         for i in range(n):
#             for j in range(i, n):
#                 if arr[j] >= arr[i]:   # if arr[j] < arr[i]:
#                     continue           #      return False
#                 else:
#                     return False
#         return True
# arr = [1, 3, 4, 5, 6, 7, 8, 9, 10]
# a = Solution()
# print(a.check(arr))

'''↓ More optimal with time compexitity = O(N)'''

class Solution:
    def check(self, arr):
        n = len(arr)
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                return False
        return True
arr = [1, 3, 4, 5, 6, 7, 18, 9, 14, 15]
a = Solution()
print(a.check(arr))