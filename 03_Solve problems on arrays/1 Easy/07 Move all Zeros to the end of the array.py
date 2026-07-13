# class Solution:
#     def move_zeros(self, arr):
#         n = len(arr)
#         temp = [0] * n
#         index = 0
#         for i in arr:
#             if i != 0:
#                 temp[index] = i
#                 index += 1
#         for i in range(n):
#             arr[i] = temp[i]
# arr = [0, 1, 2, 0 , 3, 4, 0 , 5, 0]
# a = Solution()
# a.move_zeros(arr)
# print(arr)

'''↓ Optimal approach for space compexity'''

class Solution:
    def move_zero(self, arr):
        j = -1
        for i in arr:
            if i == 0:
                j = i
                break
        if j == -1:
            return
        for i in range(j+1, len(arr)):
            if arr[i] != 0:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
arr = [0, 1, 2, 0 , 3, 4, 0 , 5, 0]
a = Solution()
a.move_zero(arr)
print(arr)