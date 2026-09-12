'''My approach'''
# class Solution:
#     def countallSubsequences(self, index, arr, k):
#         if k == 0:
#             return 1
#         if k < 0 or index == len(arr):
#             return 0
#         return self.countallSubsequences(index+1, arr, k-arr[index]) + self.countallSubsequences(index+1, arr, k)
#     def main(self, arr, k):
#         return "Yes" if 0 < self.countallSubsequences(0, arr, k) else "No"
# if __name__ == "__main__":
#     arr = [1, 3, 4, 5, 6]
#     k = 2
#     print(Solution().main(arr, k))


'''approach'''
class Solution:
    def countallSubsequences(self, index, arr, k):
        if k == 0:
            return True
        if k < 0:
            return False
        if index == len(arr):
            return k == 0
        return self.countallSubsequences(index+1, arr, k-arr[index]) or self.countallSubsequences(index+1, arr, k)
    def main(self, arr, k):
        return self.countallSubsequences(0, arr, k)
if __name__ == "__main__":
    arr = [1, 3, 4, 5, 6]
    k = 2
    print(Solution().main(arr, k))