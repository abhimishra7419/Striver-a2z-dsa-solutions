'''My approach - I'''
# class Solution:
#     def isOdd(self, n):
#         return n%2 == 1
# if __name__ == "__main__":
#     n = 42
#     a = Solution()
#     print(a.isOdd(n))

'''My approach - II'''
class Solution:
    def isOdd(self, n):
        return n & 1 == 1

    
if __name__ == "__main__":
    n = 42
    a = Solution()
    print(a.isOdd(n))