'''My brute force'''
# class Solution:
#     def finding_root(self, M, n):
#         x = -1
#         for i in range(M+1):
#             if M == i**n:
#                 x = i
#             if M < i**n:
#                 break
#         return x
# a = Solution()
# print(a.finding_root(0, 5))

'''My Optimal approach'''
class Solution:
    def finding_root(self, M, n):
        low = 0
        high = M
        while low <= high:
            mid = (low + high) //2
            result = 1
            for _ in range(n):   # so we can avoid compute very large number again and again
                result *= mid
                if result > M:
                    break
            if result == M:
                return mid
            if result < M:
                low = mid + 1
            else:
                high = mid - 1
        return -1
a = Solution()
print(a.finding_root(27, 3))