'''Brute force approach'''
# class Solution:
#     def sum_check(self, arr, target):
#         n = len(arr)
#         for i in range(n):
#             for j in range(i+1, n):
#                 if arr[i] + arr[j] == target:
#                     return "Yes"
#         return "No"
# arr = [2,6,5,8,11]
# a = Solution()
# print(a.sum_check(arr, 14))
# print(a.sum_check(arr, 15))


'''My approach'''
class Solution:
    def sum_check(self, arr, target):
        n = len(arr)
        for i in range(n):
            if target - arr[i] in arr and target - arr[i] != arr[i]:
                return "Yes"
        return "No"
arr = [2,6,5,8,11]
a = Solution()
print(a.sum_check(arr, 14))
print(a.sum_check(arr, 15))

'''Better approach'''
# class Solution:
#     def sum_check(self, arr, target):
#         n = len(arr)
#         dict = {}
#         for index, value in enumerate(arr):
#             compliment = target - value
#             if compliment in dict:
#                 return "Yes"
#             dict[value] = index
#         return "No"
# arr = [2,6,5,8,11]
# a = Solution()
# print(a.sum_check(arr, 14))
# print(a.sum_check(arr, 15))



'''Optimal approach'''
# class Solution:
#     def sum_check(self, arr, target):
#         n = len(arr)
#         arr = sorted(arr)
#         left, right = 0, n-1
#         while left < right:
#             if arr[left] + arr[right] == target:
#                 return "Yes"
#             elif arr[left] + arr[right] < target:
#                 left += 1
#             else:
#                 right -= 1
#         return "N0"
# arr = [2,6,5,8,11]
# a = Solution()
# print(a.sum_check(arr, 14))
# print(a.sum_check(arr, 15))