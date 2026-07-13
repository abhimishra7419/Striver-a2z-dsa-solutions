class solution:
    def name(self, count, name, n):
        if count == n:
            return
        print(name, end="")
        self.name(count+1, name, n)
if __name__ == "__main__":
    a = solution()
    a.name(0, "Tony ", 5)