'''My Brute force'''
# class Solution:
#     def setRightmostUnsetBit(self, n):
#         bianary = ""
#         Flag = True
#         a = n
#         while (n > 0):
#             bianary += str(n%2)
#             n //= 2
#         bianary = list(bianary)
#         for i in range(len(bianary)):
#             if bianary[i] == '0':
#                 bianary[i] = '1'
#                 Flag = False
#                 break
#         if Flag:
#             return a
#         n = 0
#         for i in range(len(bianary)):
#             n += (int(bianary[i])*(2**i))
#         return n
# if __name__ == "__main__":
#     n = 10
#     a = Solution()
#     print(a.setRightmostUnsetBit(n))

'''Optimal apporach'''
class Solution:
    def setRightmostUnsetBit(self, n):
        if n & (n + 1) == 0:
            return n
        return n | (n + 1)
if __name__ == "__main__":
    n = 1
    a = Solution()
    print(a.setRightmostUnsetBit(n))