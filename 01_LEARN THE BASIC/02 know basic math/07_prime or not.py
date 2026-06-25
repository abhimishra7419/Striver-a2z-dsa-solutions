# class solution:
#     def primeNO(self, n):
#         for i in range(2, n):
#             if n % i == 0:
#                 return False
#         return True
# a = solution()
# print(a.primeNO(2))
# print(a.primeNO(3))
# print(a.primeNO(25))
# print(a.primeNO(12))

import math
def primeNo(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
print(primeNo(2))
print(primeNo(4))
print(primeNo(3))
print(primeNo(12))
print(primeNo(13))