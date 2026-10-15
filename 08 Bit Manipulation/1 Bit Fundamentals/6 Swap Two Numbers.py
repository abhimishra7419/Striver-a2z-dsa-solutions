'''My approach'''
# class Solution:
#     def swaping(self, a, b):
#         a, b = b, a
#         return [a, b]
# if __name__ == "__main__":
#     a = 5
#     b = 10
#     obj = Solution()
#     print(obj.swaping(a, b))


'''My Arithmetic approach'''
# class Solution:
#     def swaping(self, a, b):
#         a = a + b 
#         b = a - b
#         a = a - b
#         return [a, b]
# if __name__ == "__main__":
#     a = 5
#     b = 10
#     obj = Solution()
#     print(obj.swaping(a, b))


'''My XOR approach'''
class Solution:
    def swaping(self, a, b):
        a = b ^ a
        b = a ^ b
        a = b ^ a
        return [a, b]
if __name__ == "__main__":
    a = 5
    b = 10
    obj = Solution()
    print(obj.swaping(a, b))