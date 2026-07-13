'''My approach (Brute force)'''
# class Solution:
#     def find_triplets(self, arr):
#         n = len(arr)
#         st = set()
#         for i in range(n):
#             for j in range(i):
#                 for k in range(j):
#                     if arr[i] + arr[j] + arr[k] == 0:
#                         st.add(tuple(sorted([arr[i], arr[j], arr[k]])))
#         return list(st)
# arr1 = [-1,0,1,2,-1,-4]
# arr2 = [-1,0,1,0]
# a = Solution()
# print(a.find_triplets(arr1))
# print(a.find_triplets(arr2))

'''Better approach'''
# class Solution:
#     def find_triplets(self, arr):
#         n = len(arr)
#         ans = set()
#         for i in range(n):
#             hashset = set()
#             for j in range(i+1, n):
#                 third_element = -(arr[i] + arr[j])
#                 if third_element in hashset:
#                     triplets = tuple(sorted([arr[i], arr[j], third_element]))
#                     ans.add(triplets)
#                 hashset.add(arr[j])
#         return[list(triplets) for triplets in ans]
# arr1 = [-1,0,1,2,-1,-4]
# a = Solution()
# res = a.find_triplets(arr1)
# for triplets in res:
#     print(triplets)

'''Optimal approach'''
class Solution:
    def find_triplets(self, arr):
        n = len(arr)
        arr.sort()
        ans = []
        for i in range(n):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            left, right = i+1, n-1
            while  left < right:
                total = arr[i] + arr[left] + arr[right]
                if total == 0:
                    ans.append([arr[i], arr[left], arr[right]])
                    left += 1
                    right -= 1
                    while left < right and arr[left] == arr[left-1]:
                        left += 1
                    while left < right and arr[right] == arr[right+1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else :
                    right -= 1
        return ans
arr1 = [-1,0,1,2,-1,-4]
arr2 = [0, 0, 0]
a = Solution()
print(a.find_triplets(arr1))
print(a.find_triplets(arr2))