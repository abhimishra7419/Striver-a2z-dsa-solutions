# class solution:
#     def divisors(self, n):
#         list = []
#         for i in range(1, n+1):
#             if n % i == 0:
#                 list.append(i)
#         return list
# a = solution()
# print(a.divisors(12))

# ↑ it's compaxcity is O(n) but we need O(sqrt(n))

import math
def divisors(n):
    list = []
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            list.append(i)
            if n // i != i:
                list.append(n//i)
    return sorted(list)

print(divisors(12))