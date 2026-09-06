'''Optimal approach'''
class Solution:
    def insert(self, stack, temp):
        if not stack or stack[-1] <= temp:
            stack.append(temp)
            return
        val = stack.pop()
        self.insert(stack, temp)
        stack.append(val)

    def sortStack(self, stack):
        if stack:
            temp = stack.pop()
            self.sortStack(stack)
            self.insert(stack, temp)

# Main function
if __name__ == "__main__":
    stack = [4, 1, 3, 2]
    Solution().sortStack(stack)

    # Print the sorted stack
    print("Sorted stack (descending order):", stack)