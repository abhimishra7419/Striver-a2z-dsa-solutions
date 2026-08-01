'''Brute force'''
# class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     if not s:
    #         return ""
            
    #     start, end = 0, 0
        
    #     def expand_around_center(left: int, right: int) -> int:
    #         # Expand outwards as long as characters match and indices are in bounds
    #         while left >= 0 and right < len(s) and s[left] == s[right]:
    #             left -= 1
    #             right += 1
    #         # Return the length of the palindrome found
    #         return right - left - 1

    #     for i in range(len(s)):
    #         # Case 1: Odd length palindromes (e.g., "aba", center is 'b')
    #         len1 = expand_around_center(i, i)
            
    #         # Case 2: Even length palindromes (e.g., "abba", center is between 'b' and 'b')
    #         len2 = expand_around_center(i, i + 1)
            
    #         # Find the maximum length between the two cases
    #         max_len = max(len1, len2)
            
    #         # Update the boundaries of the longest palindrome found so far
    #         if max_len > (end - start):
    #             start = i - (max_len - 1) // 2
    #             end = i + max_len // 2
                
    #     return s[start : end + 1]


'''Optimal approach'''
class Solution:
    def palindromicSubstring(self, s):
        if not s:
            return ""

        T = "^#" + "#".join(s) + "#$"
        n = len(T)
        P = [0] * n  # Array to store palindrome radius at each center
        C = 0        # Center of the current furthest-reaching palindrome
        R = 0        # Right boundary of the current furthest-reaching palindrome
        for i in range(1, n - 1):
            i_mirror = 2 * C - i
            if R > i:
                P[i] = min(R - i, P[i_mirror])
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
            if i + P[i] > R:
                C = i
                R = i + P[i]
        max_len, center_index = max((val, idx) for idx, val in enumerate(P))
        start = (center_index - 1 - max_len) // 2
        return s[start : start + max_len]
s = "abcbaa"
a = Solution()
print(a.palindromicSubstring(s))
