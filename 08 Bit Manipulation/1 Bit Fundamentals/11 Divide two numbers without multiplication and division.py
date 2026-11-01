'''Optimal Solution'''
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Determine the sign
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive values
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            # Find the largest doubled divisor that fits
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        # Apply the sign
        if negative:
            quotient = -quotient

        # Handle 32-bit integer overflow
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        return min(max(quotient, INT_MIN), INT_MAX)

a = Solution()
dividend = 10
divisor = 3
print(a.divide(dividend, divisor))