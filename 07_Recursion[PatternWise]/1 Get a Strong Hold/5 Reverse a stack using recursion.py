'''My approach''' # better for speed
# class Solution:
#     def helper(self, stack, rev_stack):
#         if not stack:
#             return rev_stack
#         temp = stack.pop()
#         rev_stack.append(temp)
#         return self.helper(stack, rev_stack)
#     def reverseStack(self, stack):
#         rev_stack = []
#         return self.helper(stack, rev_stack)
# if __name__ == "__main__":
#     stack = [1, 2, 3, 4, 5, 6, 7, 8]
#     a = Solution()
#     print(a.reverseStack(stack))


'''It comes down to a strict rule in low-level programming called In-Place Manipulation.
In some systems (like embedded software, microcontrollers, or video game engines),memory is incredibly
scarce. If you have a stack taking up 4GB of RAM, your code would require another 4GB of RAM to
create rev_stack. The system might crash from running out of memory.The "In-Place" solution is a
purely theoretical exercise to see if a candidate can manipulate memory without allocating a single
new variable, sacrificing speed to save physical memory.'''

'''Approach''' # better for memory
class Solution:
    def helper(self, stack, item):
        if not stack:
            stack.append(item)
            return
        temp = stack.pop()
        self.helper(stack, item)
        stack.append(temp)
    def reverseStack(self, stack):
        if stack:
            temp = stack.pop()
            self.reverseStack(stack)
            self.helper(stack, temp)
        return stack
if __name__ == "__main__":
    stack = [1, 2, 3, 4, 5, 6, 7, 8]
    a = Solution()
    print(a.reverseStack(stack))