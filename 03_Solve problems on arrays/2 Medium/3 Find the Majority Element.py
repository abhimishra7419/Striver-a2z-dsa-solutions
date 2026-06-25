'''brute force'''
# class Solution:
#     def MajorityElement(self, arr):
#         n = len(arr)
#         for i in range(n):
#             repeating = 0
#             for j in range(i+1, n):
#                 if arr[j] == arr[i]:
#                     repeating += 1
#             if repeating > n//2:
#                 return arr[i]
#         return "There is no Majority Element"
# a = Solution()
# arr = [1, 3, 4, 5, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# print(a.MajorityElement(arr))

'''Better Approach'''
# class Solution:
#     def MajorityElement(self, arr):
#         n = len(arr)
#         mp = {}
#         for i in arr:
#             if i in mp:
#                 mp[i] += 1
#             else:
#                 mp[i] = 1
#         for num, count in mp.items():
#             if count > n//2:
#                 return num
#         return -1 , ("error")
# a = Solution()
# arr = [1, 3, 4, 5, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# print(a.MajorityElement(arr))

'''Optimal Approach'''
class Solution:
    def MajorityElement(self, arr):
        n = len(arr)
        count = 0
        element = 0
        for i in arr:
            if count == 0:
                count = 1
                element = i
            elif element == i:
                count += 1
            else:
                count -= 1
        count1 = arr.count(element)
        if count1 > n//2:
            return element
        return -1
a = Solution()
arr = [1, 3, 4, 5, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
print(a.MajorityElement(arr))