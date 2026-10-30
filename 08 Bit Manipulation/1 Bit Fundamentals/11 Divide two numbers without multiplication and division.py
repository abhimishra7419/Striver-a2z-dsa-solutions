'''Optimal Solution'''
class Solution:
    def divide(self, dividend, divisor):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        sign = True
        if dividend < 0 and divisor > 0:
            sign = False
        if dividend >= 0 and divisor < 0:
            sign = False
        count = 0
        while (dividend < divisor):
            