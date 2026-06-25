# class Solution:
#     def remove_duplicates(self, arr):
#         seen = set()
#         k = 0
#         for a in arr:
#             if a not in seen:
#                 seen.add(a)
#                 arr[k] = a
#                 k += 1
#         return k
# arr = [1, 2, 2, 4, 4, 6, 6, 7, 8, 9, 9]
# a = Solution()
# k = a.remove_duplicates(arr)
# print("The number of unique element is :",k)
# print(arr[:k])

'''↓ Optimal code'''

class Solution:
    def remove_duplicates(self, arr):
        k = 1
        n = len(arr)
        for i in range(1, n):
            if arr[i] > arr[k-1]:
                arr[k] = arr[i]
                k += 1
        return k
arr = [1, 2, 2, 4, 4, 6, 6, 7, 8, 9, 9]
a = Solution()
k = a.remove_duplicates(arr)
print("The number of unique element is :",k)
print(arr[:k], end= "")