# class Solution:
#     def finding(self, arr):
#         n = len(arr)
#         arr = sorted(arr)
#         smallest = arr[0]
#         largest = arr[n-1]
#         for k in arr:
#             if smallest <= largest:
#                 if k != smallest:
#                     return f"The missing number is {smallest}"
#             smallest += 1
#         return "Nothing is missing"
# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# a = Solution()
# print(a.finding(arr))

'''↓ Optimal apprcoah'''
class Solution:
    def finding(self, arr):
        n = len(arr) + 1
        xor1 = 0
        xor2 = 0
        for i in range(n - 1):
            xor2 ^= arr[i]
        for i in range(1, n + 1):
            xor1 ^= i
        return xor1 ^ xor2
arr = [1, 2, 3, 4, 5, 7, 8]
a = Solution()
print(a.finding(arr))
