'''My approach''' # memory is good
# class Solution:
#     def combinationSum(self, index, curr, arr, target, n, res):
#         if sum(curr) == target:
#             return res.append(list(curr))
#         if index == n:
#             return
#         if sum(curr) > target:
#             return 
#         curr.append(arr[index])
#         self.combinationSum(index, curr, arr, target, n, res)
#         curr.pop()
#         self.combinationSum(index+1, curr, arr, target, n, res)
#     def main(self, arr, target):
#         res = []
#         curr = []
#         n = len(arr)
#         self.combinationSum(0, curr, arr, target, n, res)
#         return res
# if __name__ == "__main__":
#     arr = [2,3,6,7]
#     Target = 7
#     a = Solution()
#     print(a.main(arr, Target))


'''My approach''' # little bit time improvement
# class Solution:
#     def combination(self, index, curr, arr, target, n, res, s):
#         if s == target:
#             return res.append(list(curr))
#         if index == n:
#             return
#         if s > target:
#             return
#         curr.append(arr[index])
#         self.combination(index, curr, arr, target, n, res, s+arr[index])
#         curr.pop()
#         self.combination(index+1, curr, arr, target, n, res, s)
#     def main(self, arr, target):
#         res = []
#         curr = []
#         n = len(arr)
#         self.combination(0, curr, arr, target, n, res, 0)
#         return res
# if __name__ == "__main__":
#     arr = [2,3,1,7]
#     Target = 7
#     a = Solution()
#     print(a.main(arr, Target))


'''approach'''
class Solution:
    def findCombination(self, ind, target, arr, ans, ds):
        if ind == len(arr):
            if target == 0:
                ans.append(list(ds))
            return
        if arr[ind] <= target:
            ds.append(arr[ind])
            self.findCombination(ind, target - arr[ind], arr, ans, ds)
            ds.pop()
        self.findCombination(ind + 1, target, arr, ans, ds)
    def combinationSum(self, candidates, target):
        ans = []
        ds = [] 
        self.findCombination(0, target, candidates, ans, ds)
        return ans

# Driver code
if __name__ == "__main__":
    obj = Solution()
    v = [2, 3, 6, 7]
    target = 7
    print(obj.combinationSum(v, target))