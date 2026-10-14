'''My brute force'''
# class Solution:
#     def power(self, n):
#         if n <= 0:
#             return False
#         while n > 2:
#             if n % 2 != 0:
#                 return False
#             n //= 2
#         return True
# if __name__ == "__main__":
#     n = 16
#     a = Solution()
#     print(a.power(n))

'''Optimal'''
class Solution:
    def power(self, n):
        if n <= 0:
            return False
        return (n & (n-1)) == 0
if __name__ == "__main__":
    n = 16
    a = Solution()
    print(a.power(n))