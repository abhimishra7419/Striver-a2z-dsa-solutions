# class solution:
#     def findfactor(self, x, y):
#         r = min(x, y)
#         factors = []
#         for i in range(1, r+1):
#             if x % i == 0 and y % i == 0:
#                 factors.append(i)
#         HCF = max(factors)
#         return HCF
# a = solution()
# print(a.findfactor(12, 18))
# print(a.findfactor(12, 12))
# print(a.findfactor(50, 42))
# print(a.findfactor(40, 100))

# ↓ PRO version (It's complaxity is low compare to my code)

class solution:
    def findfactor(self, x, y):
        while y != 0:
            x, y = y, x%y
        return x
a = solution()
print(a.findfactor(12, 18))
print(a.findfactor(12, 12))
print(a.findfactor(50, 42))
print(a.findfactor(40, 100))