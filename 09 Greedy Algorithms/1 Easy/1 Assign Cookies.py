class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()

        i = 0  # Child pointer
        j = 0  # Cookie pointer

        while i < len(g) and j < len(s):

            if s[j] >= g[i]:
                i += 1

            j += 1

        return i
