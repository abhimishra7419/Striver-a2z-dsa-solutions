'''Brute force'''
# class Solution:
#     def ReverseString(self, s):
#         words = []
#         word = ""
#         for char in s:
#             if char != ' ':
#                 word += char
#             else:
#                 words.append(word)
#                 word = ""
#         if word:
#             words.append(word)
#         words.reverse()
#         return " ".join(words)
# s = "welcome to the jungle       "
# a = Solution()
# print(a.ReverseString(s))



'''Better approach'''
# class Solution:
#     def ReverseString(self, s):
#         word = s.split()
#         word.reverse()
#         return " ".join(word)
# s = "welcome to the jungle"
# a = Solution()
# print(a.ReverseString(s))


'''Optimal approach'''
class Solution:
    def ReverseString(self, s):
        result = ""
        i = len(s)-1
        while i >= 0:
            while i >= 0 and s[i] == ' ':
                i -= 1
            
            if i < 0:
                break

            end = i

            while i >= 0 and s[i] != " ":
                i -= 1
            word = s[i+1:end+1]
            
            if result != "":   # Also can be "if result:"
                result += ' '
            result += word
        
        return result
s = "welcome to the jungle"
a = Solution()
print(a.ReverseString(s))
