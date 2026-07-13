class Solution:
    def fibonacci(self, n):
        if n == 0:
            return "0"
        num = 0
        arr = [0, 1]
        for i in range(2, n+1):
            num = arr[i-2] + arr[i-1]
            arr.append(num)
        return " ".join(map(str, arr))
a = Solution()
print(a.fibonacci(0))
print(a.fibonacci(1))
print(a.fibonacci(7))
print(a.fibonacci(8))