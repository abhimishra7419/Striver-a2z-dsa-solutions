'''My brute force'''
# class Solution:
#     def checking(self, n, i):
#         bianary = ""
#         while (n > 0):
#             if n % 2 == 1:
#                 bianary += '1'
#             else:
#                 bianary += '0'
#             n //= 2
#         if len(bianary) <= i:
#             return False
#         if bianary[i] == "0":
#             return False
#         return True
# if __name__ == "__main__":
#     n = 1
#     i = 31
#     a = Solution()
#     print(a.checking(n, i))

'''Optimal approach'''
class Solution:
    def checking(slef, n, i):
        return ((n >> i) & 1) == 1
if __name__ == "__main__":
    n = 5
    i = 0
    a = Solution()
    print(a.checking(n, i))