'''My brute force'''
# class Solution:
#     def poshelper(self, x, n):
#         if n == 0:
#             return 1.0
#         res = self.poshelper(x, n-1)
#         x *= res
#         return x
#     def neghelper(self, x, n):
#         if n == 0:
#             return 1.0
#         res = self.neghelper(x, n+1)
#         x *= res
#         return x
#     def pow(self, x, n):
#         if n == 0:
#             return 1.0
#         INT_min, INT_max = -2**31, (2**31)-1
#         if n > 0:
#             x = self.poshelper(x, n)
#         else:
#             x = self.neghelper(1/x, n)
#         if x <= INT_min: return INT_min
#         if x >= INT_max: return INT_max
#         return x
# if __name__ == '__main__':
#     x = 2.0000
#     n = 10
#     a = Solution()
#     print(a.pow(x, n))

'''Optimial approach'''
class Solution:
    def power(self, x, n):
        if n == 0:
            return 1.0
        if n == 1:
            return x
        if n%2 == 0:
            return self.power(x*x, n//2)
        return x*self.power(x, n-1)
    def pow(self, x, n):
        if n < 0:
            return 1.0/ self.power(x, -n)
        return self.power(x, n)
if __name__ == '__main__':
    x = 2.0000
    n = 10
    a = Solution()
    print(a.pow(x, n))