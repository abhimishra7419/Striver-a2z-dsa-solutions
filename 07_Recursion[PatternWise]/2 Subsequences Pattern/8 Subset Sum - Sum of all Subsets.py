'''Brute force'''
# class Solution:
#     def subsetsum(self, s):
#         n = len(s)
#         total = 1 << n
#         subsets = []
#         for mask in range(total):
#             subset = []
#             for i in range(n):
#                 if mask & (1 << i):
#                     subset.append(s[i])
#             subsets.append(sum(subset))
#         subsets.sort()
#         return subsets
# if __name__ == "__main__":
#     arr = [5,2,1]
#     a = Solution()
#     print(a.subsetsum(arr))



    
'''My Recursive approach'''
class Solution:
    def helper(self, index, arr, curr, res):
        if index == len(arr):
            res.append(sum(curr))
            return
        curr.append(arr[index])
        self.helper(index+1, arr, curr, res)
        curr.pop()
        self.helper(index+1, arr, curr, res)
    def main(self, arr):
        res = []
        curr = []
        self.helper(0, arr, curr, res)
        res.sort()
        return res
if __name__ == "__main__":
    arr = [5,2,1]
    a = Solution()
    print(a.main(arr))