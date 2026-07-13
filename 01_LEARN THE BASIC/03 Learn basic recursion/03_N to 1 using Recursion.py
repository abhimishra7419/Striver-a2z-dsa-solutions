class solution:
    def printNo(self, n):
        if n < 1:
            return
        print(n)
        self.printNo(n-1)
if __name__ == "__main__":
    a = solution()
    a.printNo(5)