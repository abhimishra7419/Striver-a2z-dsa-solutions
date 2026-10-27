'''My Optimal Solution'''
class Solution:
    def isPerfect(self, n: int) -> bool:
        if n <= 1:
            return False
        ans = 1
        i = 2
        while i*i <= n:
            if (n%i) == 0:
                ans += i
                pair = n//i
                if pair != i:
                    ans += pair
            i += 1
        return ans == n
a = Solution()
print(a.isPerfect(28))