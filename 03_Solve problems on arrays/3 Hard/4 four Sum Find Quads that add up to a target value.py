'''Brute force'''
# class Solution:
#     def find_quads(self, arr, target):
#         n = len(arr)
#         ans = set()
#         for i in range(n):
#             for j in range(i+1, n):
#                 for k in range(j+1, n):
#                     for l in range(k+1, n):
#                         if arr[i] + arr[j] + arr[k] + arr[l] == target:
#                             temp = tuple(sorted([arr[i], arr[j], arr[k], arr[l]]))
#                             ans.add(temp)
#         return [list(quads) for quads in ans]
# arr1 = [2, 2, 2, 2, 2]
# target = 8
# a = Solution()
# print(a.find_quads(arr1, target))

'''Better approach'''
# class Solution:
#     def find_quads(self, arr, target):
#         n = len(arr)
#         ans = set()
#         for i in range(n):
#             seen = set()
#             for j in range(i+1, n):
#                 for k in range(j+1, n):
#                     requried = target - arr[i] + arr[j] + arr[k]
#                     if requried in seen:
#                         quad = tuple(sorted([arr[i], arr[j], arr[k], requried]))
#                         ans.add(quad)
#                     seen.add(requried)
#         return [list(quads) for quads in ans]

# arr1 = [2, 2, 2, 2, 2]
# target = 8
# a = Solution()
# print(a.find_quads(arr1, target))

'''Optimal approach'''
class Solution:
    def find_quads(self, arr, target):
        n = len(arr)
        arr.sort()
        result = []
        for i in range(n):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            for j in range(i+1, n):
                if j > i+1 and arr[j] == arr[j-1]:
                    continue
                left, right = j+1, n-1
                while left < right:
                    current = arr[i] + arr[j] + arr[left] + arr[right]
                    if current == target:
                        result.append([arr[i], arr[j],  arr[left], arr[right]])
                        while left < right and arr[left] == arr[left+1]:
                            left += 1
                        while left < right and arr[right] == arr[right-1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif current < target:
                        left += 1
                    else:
                        right -= 1
        return result
arr1 = [1,0,-1,0,-2,2]
target = 0
a = Solution()
print(a.find_quads(arr1, target))