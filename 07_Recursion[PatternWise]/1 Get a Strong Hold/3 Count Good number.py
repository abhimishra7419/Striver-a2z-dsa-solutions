'''Opitimal approach'''
# class Solution:
#     def count_good_numbers(self, index, n):
#         MOD = 10**9 + 7
#         if index == n:
#             return 1
#         result = 0
#         if index % 2 == 0:  
#             even_digits = [0, 2, 4, 6, 8]
#             for digit in even_digits:
#                 result = (result + self.count_good_numbers(index + 1, n)) % MOD
#         else:
#             prime_digits = [2, 3, 5, 7]
#             for digit in prime_digits:
#                 result = (result + self.count_good_numbers(index + 1, n)) % MOD
#         return result

# # Main function
# if __name__ == "__main__":
#     n = 1
#     a = Solution()
#     print(a.count_good_numbers(0, n))

'''For leetcode'''
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        
        even_positions = (n + 1) // 2
        odd_positions = n // 2
        
        # Calculate combinations using modular exponentiation
        even_choices = pow(5, even_positions, MOD)
        odd_choices = pow(4, odd_positions, MOD)
        
        return (even_choices * odd_choices) % MOD