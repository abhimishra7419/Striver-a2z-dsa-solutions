'''My approach'''
class Solution:
    def helper(self, index, arr, curr, res):
        if index == len(arr):
            res.add(tuple(curr))
            return
        curr.append(arr[index])
        self.helper(index+1, arr, curr, res)
        curr.pop()
        self.helper(index+1, arr, curr, res)
    def main(self, arr):
        arr.sort()
        res = set()
        curr = []
        self.helper(0, arr, curr, res)
        res = list(res)
        for _ in range(len(res)):
            item = list(res.pop())
            res.insert(0, item)
        return res
if __name__ == "__main__":
    arr = [4,4,4,1,4]
    a = Solution()
    print(a.main(arr))