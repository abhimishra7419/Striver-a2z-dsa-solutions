'''My approach'''
# class Solution:
#     def atoi(self, s):
#         val = 0
#         sing = 0
#         pervious = -1
#         for chr in s:
#             if chr == ' ' and (val != 0 or sing != 0 or pervious == 0):
#                 break
#             elif chr == ' ':
#                 continue
#             elif chr == '0' and val == 0:
#                 pervious = 0
#                 continue
#             elif (chr == '-' or chr == '+') and (pervious == 0 or sing == -1 or sing == 1 or val != 0):
#                 break
#             elif chr == '+':
#                 sing = 1
#                 continue
#             elif chr == '-':
#                 sing = -1
#                 continue
#             elif chr.isdigit():
#                 val = val*(10) + int(chr)
#             else:
#                 break
#         if val != 0 and sing == 0:
#             sing = 1
#         val = val*sing
#         if (-2**31) > val:
#             return (-2**31)
#         if val > (2**31)-1:
#             return (2**31)-1
#         return val
# s =  "0  123"
# a = Solution()
# print(a.atoi(s))


'''simple approach'''
class Solution:
    def atoi(self, s):
        int_min = (-2**31)
        int_max = (2**31)-1

        i = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i += 1

        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            num = num*10 + digit
            i += 1

        num *= sign
        if int_min > num:
            return int_min
        elif int_max < num:
            return int_max

        return num
s =  "0  123"
a = Solution()
print(a.atoi(s))