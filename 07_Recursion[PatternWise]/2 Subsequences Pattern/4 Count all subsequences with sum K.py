'''My approach'''
class Solution:
    def countallSubsequences(self, index, arr, k):
        if k == 0:
            return 1
        if k < 0 or index == len(arr):
            return 0
        return self.countallSubsequences(index+1, arr, k-arr[index]) + self.countallSubsequences(index+1, arr, k)
    def main(self, arr, k):
        return self.countallSubsequences(0, arr, k)
if __name__ == "__main__":
    arr = [1, 2, 1]
    k = 2
    print(Solution().main(arr, k))