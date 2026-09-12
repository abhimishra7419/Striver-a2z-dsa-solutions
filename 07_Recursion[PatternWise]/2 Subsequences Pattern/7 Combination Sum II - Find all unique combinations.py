'''My approach'''
# class Solution:
#     def findingCombination(self, index, curr, target, arr, res):
#         if index == len(arr):
#             if target == 0 and list(curr) not in res:
#                 res.append(list(curr))
#             return
#         if arr[index] <= target:
#             curr.append(arr[index])
#             self.findingCombination(index+1, curr, target-arr[index], arr, res)
#             curr.pop()
#         self.findingCombination(index+1, curr, target, arr, res)
#     def main(self, arr, target):
#         res = []
#         curr = []
#         arr.sort()
#         self.findingCombination(0, curr, target, arr, res)
#         return res
# if __name__ == "__main__":
#     obj = Solution()
#     v = [10,1,2,7,6,1,5]
#     target = 8
#     print(obj.main(v, target))



'''Approach'''
class Solution:
    def findCombination(self, ind, target, arr, ans, ds):
        if target == 0:
            ans.append(list(ds))
            return
        for i in range(ind, len(arr)):
            if i > ind and arr[i] == arr[i - 1]:
                continue
            if arr[i] > target:
                break
            ds.append(arr[i])
            self.findCombination(i + 1, target - arr[i], arr, ans, ds)
            ds.pop()
    def combinationSum2(self, candidates, target):
        candidates.sort()
        ans = []
        ds = []
        self.findCombination(0, target, candidates, ans, ds)
        return ans

# Driver code
if __name__ == "__main__":
    obj = Solution()
    v = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    comb = obj.combinationSum2(v, target)