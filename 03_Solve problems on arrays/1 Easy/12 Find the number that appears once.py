# class Solution:
#     def find_element(self, arr):
#         n = len(arr)
#         for i in range(n):
#             num = arr[i]
#             count = 0
#             for j in range(n):
#                 if num == arr[j]:
#                     count += 1
#             if count == 1:
#                 return num
#         return -1
# arr = [1, 1, 2, 1, 2, 4]
# a = Solution()
# print(a.find_element(arr))


''' Another brute force ↓'''
# class Solution:   # in this approch we using numbers as index
#     def find_element(slef, arr):
#         n = len(arr)
#         maxi = max(arr)
#         hash_arr = [0] * (maxi+1)
#         for num in arr:
#             hash_arr[num] += 1
#         for num in arr:
#             if hash_arr[num] == 1:
#                 return num
#         return -1
# arr = [1, 1, 2, 1, 2, 4]
# a = Solution()
# print(a.find_element(arr))



'''Another brute force ↓ (My approch)'''
# class Solution:
#     def find_element(self, arr):
#         freq = {}
#         for num in arr:
#             freq[num] = freq.get(num, 0) + 1
#         return [key for key, value in freq.items() if value == 1]   # To use value to return key
# arr = [1, 1, 2, 1, 2, 4]
# a = Solution()
# print(a.find_element(arr))



''' Optimal approcah ↓'''
class Solution:  # if number appares twice or (even times) its working well otherwise its gives wrong answer
    def find_element(self, arr):
        xorr = 0
        for num in arr:
            xorr ^= num
        return xorr
arr = [1, 1, 2, 2, 4]
a = Solution()
print(a.find_element(arr))
