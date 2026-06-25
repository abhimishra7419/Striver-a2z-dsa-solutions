'''Brute force Approach'''
# class Solution:
#     def sort(self, arr):
#         count0 = count1 = count2 = 0
#         for i in arr:
#             if i == 0:
#                 count0 += 1
#             elif i == 1:
#                 count1 += 1
#             elif i == 2:
#                 count2 += 1
#         index = 0
#         for i in range(count0):
#             arr[i] = 0
#             index += 1
#         for i in range(count1):
#             arr[index] = 1
#             index += 1
#         for i in range(count2):
#             arr[index] = 2
#             index += 1
#         return arr
# a = Solution()
# arr = [1 , 0, 2, 1, 2, 0, 1, 2, 0, 0, 1]
# print(a.sort(arr))

'''Optimal approach (Dutch National Flag algorithm)'''
class Solution:
    def dutchNationalFlag(self, arr):
        left, mid, right = 0, 0, len(arr)-1
        while mid <= right:
            if arr[mid] == 0:
                arr[left], arr[mid] = arr[mid], arr[left]
                left += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[right] = arr[right], arr[mid]
                right -= 1
        return arr     
a = Solution()
arr = [1 , 0, 2, 1, 2, 0, 1, 2, 0, 0, 1]
print(a.dutchNationalFlag(arr))