# class Solution:
#     def right_rotate(self, arr, k):
#         n = len(arr)
#         temp = arr[-k:]
#         for i in range(n-k-1, -1, -1):
#             arr[i+k] = arr[i]
#         for i in range(k):
#             arr[i] = temp[i]
#     def left_ratate(self, arr, k):
#         n = len(arr)
#         temp = arr[:k]
#         for i in range(k, n):
#             arr[i-k] = arr[i]
#         for i in range(k):
#             arr[n-i-1] = temp[-1+i]   # temp = [1, 2]
# a = Solution()
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a.right_rotate(arr, 2)
# print(arr)
# arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a.left_ratate(arr2, 2)
# print(arr2)

'''↓ Optimal Approach for space compexity(My approach)'''
# class Solution:
#     def right_rotate(self, arr, k):
#         n = len(arr)
#         for i in range(n//2):
#             arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
#         for i in range(k//2):
#             arr[i], arr[k-1-i] = arr[k-1-i], arr[i]
#         for i in range(n//2):
#             if k+i < n-1-i:
#                 arr[k+i], arr[n-1-i] = arr[n-1-i], arr[k+i]
#     def left_rotate(self, arr, k):
#         n = len(arr)
#         for i in range(k//2):
#             arr[i], arr[k-1-i] = arr[k-1-i], arr[i]
#         for i in range(n//2):
#             arr[i], arr[n-1-i] = arr[n-1-i], arr[i]
#         for i in range(n-k//2):
#             if i < n-1-k-i:
#                 arr[i], arr[n-1-k-i] = arr[n-1-k-i], arr[i]
# a = Solution()
# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# a.right_rotate(arr, 2)
# print(arr)
# arr2 = [1, 2, 3, 4, 5, 6, 7, 8]
# a.left_rotate(arr2, 2)
# print(arr2, end="")


'''Easy code and Optimal approach ↓'''

class Solution:
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    def rotateArray(self, nums, k, direction):
        n = len(nums)
        if n == 0 or k == 0:
            return nums
        k = k % n
        if direction == "right":
            self.reverse(nums, 0, n - 1)
            self.reverse(nums, 0, k - 1)
            self.reverse(nums, k, n - 1)
        elif direction == "left":
            self.reverse(nums, 0, k - 1)
            self.reverse(nums, k, n - 1)
            self.reverse(nums, 0, n - 1)
        return nums
sol = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 2
direction = "right"
result = sol.rotateArray(nums, k, direction)
print(result)
