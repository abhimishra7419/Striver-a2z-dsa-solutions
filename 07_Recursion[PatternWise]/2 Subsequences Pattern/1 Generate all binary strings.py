'''Approach'''
class Solution:
    def generator(self, n, curent, arr):
        if len(curent) == n:
            arr.append(curent)
            return
        self.generator(n, curent+"0", arr)
        if not curent or curent[-1] != '1':
            self.generator(n, curent+"1", arr)
    def binaryString(self, n):
        arr = []
        self.generator(n, "", arr)
        return arr
if __name__ == "__main__":
    n = 4
    a = Solution()
    print(a.binaryString(n))