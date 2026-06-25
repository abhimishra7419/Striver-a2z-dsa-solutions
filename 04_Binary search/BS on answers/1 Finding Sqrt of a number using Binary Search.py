'''My Brute force'''
# class Solution:
#     def finding_sqrt(self, n):
#         for i in range(n):
#             if n == i*i:
#                 return i 
#             if (i-1)*(i-1) < n < i*i:
#                 return i-1
# a = Solution()
# print(a.finding_sqrt(35))


'''Brute force'''
# class Solution:
#     def finding_sqrt(self, n):
#         ans = 0
#         for i in range(1, n):
#             if n >= i*i:
#                 ans = i
#             else:
#                 break
#         return ans
# a = Solution()
# print(a.finding_sqrt(35))


'''Optimal approach'''
class Solution:
    def finding_sqrt(self, n):
        if n < 2:
            return n
        left, right, ans = 1, n//2, 0
        while left <= right:
            mid = (left + right) //2
            if mid*mid <= n:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans
a = Solution()
print(a.finding_sqrt(35))

