'''My Brute force approach'''
# class Solution:
#     def find_elements(self, arr):
#         n = len(arr)
#         repeating = n//3
#         elements_repeated = []
#         for i in range(n):
#             count = 1
#             for j in range(i+1, n):
#                 if arr[i] == arr[j]:
#                     count += 1
#             if count > repeating and arr[i] not in elements_repeated:
#                 elements_repeated.append(arr[i])
#         return elements_repeated
# arr1 = [1, 1, 1, 1]
# arr2 = [1, 2, 1, 1, 3, 2, 2]
# a = Solution()
# print(a.find_elements(arr1))
# print(a.find_elements(arr2))

'''My Better approach'''
# class Solution:
#     def find_elements(self, arr):
#         n = len(arr)
#         result = {}
#         repeating_elements = []
#         for i in range(n):
#             result[arr[i]] = result.get(arr[i], 0) + 1
#         for key in result:
#             if n//3 < result[key]:
#                 repeating_elements.append(key)
#         return repeating_elements
# arr1 = [1, 2]
# arr2 = [1, 2, 1, 1, 3, 2, 2]
# a = Solution()
# print(a.find_elements(arr1))
# print(a.find_elements(arr2))

'''My Optimal approach'''
# most repeated elements only can be 2 

class Solution:
    def find_elements(self, arr):
        n = len(arr)
        result = []
        cnt1, cnt2 = 0, 0
        el1, el2 = float('-inf'), float('-inf')
        for num in arr:
            if cnt1 == 0 and el1 != num:
                cnt1 = 1
                el1 = num
            elif cnt2 == 0 and el2 != num:
                cnt2 = 1
                el2 = num
            elif num == el1:
                cnt1 += 1
            elif num == el2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        cnt1 = 0
        cnt2 = 0
        for num in arr:
            if el1 == num:
                cnt1 += 1
            if el2 == num:
                cnt2 += 1
        if n//3 < cnt1:
            result.append(el1)
        if n//3 < cnt2:
            result.append(el2)
        return result
arr1 = [1, 2, 2]
arr2 = [1, 2, 1, 1, 3, 2, 2]
a = Solution()
print(a.find_elements(arr1))
print(a.find_elements(arr2))