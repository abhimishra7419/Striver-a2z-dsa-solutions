'''brute force'''
# class Solution:
#     def pascal_triangle(self, num):
#         triangle = []
#         for i in range(num):
#             row = [1]*(i+1)
#             for j in range(1, i):
#                 row[j] = triangle[i-1][j-1] + triangle[i-1][j]
#             triangle.append(row)
#         return triangle
# a = Solution()
# print(a.pascal_triagle(1))
# print(a.pascal_triagle(5))

'''Better approach''' # its gives only row
# class Solution:
#     def pascal_nth_row(self, num):
#         row = []
#         val = 1
#         if num == 1:
#             row.append(val)
#             return row
#         else:
#             for i in range(1, num):
#                 val = val*(num-i)//i
#                 row.append(val)
#         return row
# a = Solution()
# print(a.pascal_nth_row(1))
# print(a.pascal_nth_row(5))

'''Optimal approach'''  # Its help to find element in pascal's triangle
class Solution:
    def find_element(self, r, c):
        n = r - 1
        k = c - 1
        result = 1
        for i in range(k):
            result *= (n-i)
            result //= (i+1)
        return result
a = Solution()
print(a.find_element(5, 3))