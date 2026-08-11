'''Brute force'''
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
# class Solution:
#     def revering(self, head):
#         stack = []
#         temp = head
#         while temp:
#             stack.append(temp.data)
#             temp = temp.next
#         temp = head
#         while temp:
#             temp.data = stack.pop()
#             temp = temp.next
#         return head
#     def printing(self, head):
#         temp = head
#         while temp:
#             print(temp.data,end="->")
#             temp = temp.next
# if __name__ == "__main__":
#     head = Node(1)
#     head.next = Node(2)
#     head.next.next = Node(3)
#     head.next.next.next = Node(4)

#     a = Solution()
#     head = a.revering(head)
#     a.printing(head)
    

'''Recursive approach'''
# class ListNode:
#     def __init__(self, val=0):
#         self.val = val
#         self.next = None

# class Solution:
#     def reverseList(self, head):
#         if head is None or head.next is None:
#             return head
#         newHead = self.reverseList(head.next)
#         front = head.next
#         front.next = head
#         head.next = None
#         return newHead
# if __name__ == "__main__":
#     # Create linked list: 1 -> 2 -> 3 -> 4 -> 5
#     head = ListNode(1)
#     head.next = ListNode(2)
#     head.next.next = ListNode(3)
#     head.next.next.next = ListNode(4)
#     head.next.next.next.next = ListNode(5)
#     sol = Solution()
#     reversed_head = sol.reverseList(head)
#     while reversed_head:
#         print(reversed_head.val, end=" ")
#         reversed_head = reversed_head.next


'''My Optimal appraoch''' # It's made singular LL to double LL. 
# class Node:
#     def __init__(self, data, next=None, perv=None):
#         self.data = data
#         self.next = next
#         self.perv = perv
# class Solution:
#     def reversing(self, head):
#         temp = head
#         while temp.next:
#             temp.next.perv = temp
#             temp = temp.next
#         while temp:
#             print(temp.data,end="->")
#             temp = temp.perv

# if __name__ == "__main__":
#     head = Node(1)
#     head.next = Node(2)
#     head.next.next = Node(3)
#     head.next.next.next = Node(4)
#     head.next.next.next.next = Node(5)

#     a = Solution()
#    a.reversing(head)


'''Optimal approach'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class Solution:
    def reversing(self, head):
        perv = None
        temp = head
        while temp:
            front = temp.next   # 1-> 2-> 3-> 4
            temp.next = perv
            perv = temp
            temp = front
        return perv
    def printLL(self, head):
        temp = head
        while temp:
            print(temp.data, end="->")
            temp = temp.next

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)

    a = Solution()
    head = a.reversing(head)
    a.printLL(head)