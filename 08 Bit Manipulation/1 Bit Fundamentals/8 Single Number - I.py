'''My approach'''
class Solution:
    def SingleNumber(self, arr):
        xor = 0
        for num in arr:
            xor ^= num
        return xor
if __name__ == "__main__":
    arr = [4, 1, 2, 1, 2]
    a = Solution()
    print(a.SingleNumber(arr))