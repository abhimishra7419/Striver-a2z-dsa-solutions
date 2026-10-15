'''My brute force'''
# class Solution:
#     def countOnes(self, n):
#         count = 0
#         while n > 0:
#             if n % 2 == 1:
#                 count += 1
#             n //= 2
#         return count
# if __name__ == "__main__":
#     n = 32
#     a = Solution()
#     print(a.countOnes(n))


'''Optimal approach'''
class Solution:
    def countOnes(self, n):
        count = 0
        while n > 0:
            n = n & (n-1)
            count += 1
        return count
    
if __name__ == "__main__":
    n = 32
    a = Solution()
    print(a.countOnes(n))