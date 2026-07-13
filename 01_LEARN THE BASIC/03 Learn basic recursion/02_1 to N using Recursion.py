# class solution:
#     def natrualNo(self, x, n):
#         if x > n:
#             return
#         print(x)
#         self.natrualNo(x+1, n)
# if __name__ == "__main__":
#     a = solution()
#     a.natrualNo(1, 5)

# also can be with only one parameter ↓

class solution:
    def printNo(self, n):
        if n < 1:
            return
        self.printNo(n-1) # 1st it's stacks all number accroding to condition and calling then returing from last to fist
        print(n)
if __name__ == "__main__":
    a = solution()
    a.printNo(5)