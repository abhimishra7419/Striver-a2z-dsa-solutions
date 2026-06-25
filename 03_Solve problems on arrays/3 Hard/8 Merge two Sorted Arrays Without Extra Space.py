'''My approach''' # Its fail when arr1 is not with free space (zeros)
# class Solution:
#     def merge(self, arr1, arr2):
#         m = len(arr1)
#         n = len(arr2)
#         j = 0
#         for i in range(m-1, m-n-1, -1):
#             if arr1[i] == 0:
#                     arr1.pop(i)
#                     arr1.append(arr2[j])
#                     j += 1
#         arr1.sort()
#         return arr1
# arr1 = [-5, -2, 4, 5, 0, 0, 0]
# arr2 = [-3, 1, 8]
# a = Solution()
# print(a.merge(arr1, arr2))

'''Optimal approach'''
class Solution:
    def merge(self, arr1, m, arr2, n):
        i = m-1
        j = n-1
        k = m+n-1
        while i >= 0 and j >= 0:
            if arr1[i] > arr2[j]:
                arr1[k] = arr1[i]
                i -= 1
            else:
                arr1[k] = arr2[j]
                j -= 1
            k -= 1
        while j >= 0:
            arr1[k] = arr2[j]
            j -= 1
            k -= 1
arr1 = [-3, -2, 4, 5, 0, 0, 0]
m = 4
arr2 = [-5, 1, 8]
n = 3
a = Solution()
a.merge(arr1, m, arr2, n)
print(arr1)