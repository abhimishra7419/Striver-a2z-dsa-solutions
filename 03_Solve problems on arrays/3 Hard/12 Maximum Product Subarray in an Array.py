'''My brute approach'''
# class Solution:
#     def Maximum_product(self, arr):
#         n = len(arr)
#         max_product = float('-inf')
#         for i in range(n):
#             product = 1
#             for j in range(i, n):
#                 product *= arr[j]
#                 max_product = max(max_product, product)
#         return max_product
# arr = [1,2,-3,0,-4,-5]
# a = Solution()
# print(a.Maximum_product(arr))

'''Optimal approach - I'''
# class Solution:
#     def Maximum_product(self, arr):
#         n = len(arr)
#         pre, suf = 1, 1
#         max_product = float('-inf')
#         for i in range(n):
#             if pre == 0:
#                 pre = 1
#             if suf == 0:
#                 suf = 1
#             pre *= arr[i]
#             suf *= arr[n-1-i]
#             max_product = max(max_product, pre, suf)
#         return max_product

# arr = [1, 2, -3, 0, -4, -5]
# a = Solution()
# print(a.Maximum_product(arr))


'''Optimal approach - II'''
class Solution:
    def Maximum_product(self, arr):
        res = arr[0]
        maxpro = arr[0]
        minpro = arr[0]
        n = len(arr)
        for i in range(n):
            current = arr[i]
            if current < 0:
                maxpro, minpro = minpro, maxpro
            maxpro = max(current, maxpro*current)
            minpro = min(current, minpro*current)
            res = max(res, maxpro, minpro)
        return res
arr = [1, 2, -3, 0, -4, -5]
a = Solution()
print(a.Maximum_product(arr))
