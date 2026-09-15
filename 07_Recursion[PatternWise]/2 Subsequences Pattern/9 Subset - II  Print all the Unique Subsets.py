'''My brute force'''
# class Solution:
#     def helper(self, index, arr, curr, res):
#         if index == len(arr):
#             res.add(tuple(curr))
#             return
#         curr.append(arr[index])
#         self.helper(index+1, arr, curr, res)
#         curr.pop()
#         self.helper(index+1, arr, curr, res)
#     def main(self, arr):
#         arr.sort()
#         res = set()
#         curr = []
#         self.helper(0, arr, curr, res)
#         res = list(res)
#         for _ in range(len(res)):
#             item = list(res.pop())
#             res.insert(0, item)
#         return res
# if __name__ == "__main__":
#     arr = [4,4,4,1,4]
#     a = Solution()
#     print(a.main(arr))


'''Optimal appraoch'''
class Solution:
    def backtrack(self, start, nums, current, result):
        result.append(list(current))
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            current.append(nums[i])
            self.backtrack(i + 1, nums, current, result)
            current.pop()

    def subsetsWithDup(self, nums):
        nums.sort()
        result = []
        self.backtrack(0, nums, [], result)
        return result

if __name__ == "__main__":
    arr = [4,4,4,1,4]
    a = Solution()
    print(a.subsetsWithDup(arr))
