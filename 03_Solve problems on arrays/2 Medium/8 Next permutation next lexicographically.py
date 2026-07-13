'''Brute force'''
# from itertools import permutations
# class Solution:
#     def next_permutation(self, arr):
#         perms = sorted(set(permutations(arr)))
#         given = tuple(arr)
#         for i in range(len(arr)):
#             if perms[i] == given:
#                 if i == len(arr)-1:
#                     return list(perms[0])
#                 return list(perms[i+1])
#         return arr
# arr = [1, 3, 2]
# a = Solution()
# print(a.next_permutation(arr))

'''Optimal force'''
class Solution:
    def next_permutation(self, arr):
        n = len(arr)
        index = -1
        for i in range(n-2, -1, -1):
            if arr[i] < arr[i+1]:
                index = i
                break
        if index == -1:
            arr.reverse()
            return arr
        for i in range(n-1, index, -1):
            if arr[i] > arr[index]:
                arr[i], arr[index] = arr[index], arr[i]
                break
        arr[index+1:] = reversed(arr[index+1:])
        return arr
arr = [5, 4, 3, 2, 1, 0, 0]
a = Solution()
print(a.next_permutation(arr))