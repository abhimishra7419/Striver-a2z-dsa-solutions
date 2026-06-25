'''Using maping technique'''
# class Solution:
#     def union(self, arr1, arr2):
#         freq = {}
#         for i in range(len(arr1)):
#             freq[arr1[i]] = freq.get(arr1[i], 0) + 1
#         for i in range(len(arr2)):
#             freq[arr2[i]] = freq.get(arr1[i], 0) + 1
#         union = sorted(freq.keys())  # convert in sorted arr(list)
#         return union
# arr1 = [1, 1, 3, 4, 4, 5, 5, 6]
# arr2 = [2, 3, 4, 5, 6]
# a = Solution()
# print(a.union(arr1, arr2))

'''↓ Using set technique'''
# class Solution:
#     def union(self, arr1, arr2):
#         seen = set()
#         for num in arr1:           # i also can be write one line instant of these two loops
#             if num not in seen:    # st = set(arr1) | set(arr2)    # it's called union of set it's automaticlly romoves dublicates
#                 seen.add(num) 
#         for num in arr2:
#             if num not in seen:
#                 seen.add(num)
#         union = sorted(seen)   # convert in sorted arr(list)
#         return union
# arr1 = [1, 1, 3, 4, 4, 5, 5, 6]
# arr2 = [2, 3, 4, 5, 6]
# a = Solution()
# print(a.union(arr1, arr2))

'''↓ Optimal apprcoah'''
class Solution:
    def union(self, arr1, arr2):
        union = []
        i, j = 0, 0
        n = len(arr1)
        m = len(arr2)
        while i < n and j < m:
            if arr1[i] < arr2[j]:
                if not union or union[-1] != arr1[i]:
                    union.append(arr1[i])
                i += 1
            elif arr1[i] > arr2[j]:
                if not union or union[-1] != arr2[j]:
                    union.append(arr2[j])
                j += 1
            else:
                if not union or union[-1] != arr1[i]:   # or != arr2[j]
                    union.append(arr1[i])
                i += 1
                j += 1
        while i < n:
            if not union or union != arr1[i]:
                union.append(arr1[i])
            i += 1
        while j < m:
            if not union or union != arr2[j]:
                union.append(arr2[j])
            j += 1
        return union
arr1 = [1, 1, 3, 4, 4, 5, 5, 6]
arr2 = [2, 3, 4, 5, 6]
a = Solution()
print(a.union(arr1, arr2), end="")