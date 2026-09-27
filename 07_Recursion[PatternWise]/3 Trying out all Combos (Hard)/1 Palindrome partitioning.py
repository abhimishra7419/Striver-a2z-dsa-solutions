'''approach'''
class Solution:
    def Palindrome(self, i, j, s):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def palindromePartition(self, i, j, n, curr, res, s):
        if j == n:
            if i == n:
                res.append(list(curr))
            return
        self.palindromePartition(i, j + 1, n, curr, res, s)
        if self.Palindrome(i, j, s):
            curr.append(s[i : j + 1])
            self.palindromePartition(j + 1, j + 1, n, curr, res, s)
            curr.pop()

    def main(self, s):
        n = len(s)
        res = []
        curr = []
        self.palindromePartition(0, 0, n, curr, res, s)
        return res

if __name__ == "__main__":
    s = "aabaa"
    a = Solution()
    print(a.main(s))
