'''approach'''
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class Solution:
#     def segregateEvenOdd(self, head):
#         if head is None or head.next is None:
#             return head
#         evenHead = evenTail = None
#         oddHead = oddTail = None
#         current = head
#         while current:
#             if current.data % 2 == 0:
#                 if not evenHead:
#                     evenHead = evenTail = current
#                 else:
#                     evenTail.next = current
#                     evenTail = current
#             else:
#                 if not oddHead:
#                     oddHead = oddTail = current
#                 else:
#                     oddTail.next = current
#                     oddTail = current
#             current = current.next
#         if not evenHead:
#             return oddHead
#         if not oddHead:
#             return evenHead
#         evenTail.next = oddHead
#         oddTail.next = None

#         return evenHead

# def printList(head):
#     while head:
#         print(head.data, end=" ")
#         head = head.next

# head = Node(17)
# head.next = Node(15)
# head.next.next = Node(8)
# head.next.next.next = Node(12)
# head.next.next.next.next = Node(10)
# head.next.next.next.next.next = Node(5)
# head.next.next.next.next.next.next = Node(4)
# sol = Solution()
# newHead = sol.oddEvenList(head)
# sol.printList(newHead)



'''Modify for Leetcode'''
class Node:
    def __init__(self, val=0, next=None):
        self.data = val
        self.next = next
class Solution:
    def oddEvenList(self, head):
        if head is None or head.next is None:
            return head
        odd = head
        even = head.next
        evenhead = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenhead
        return head
    def printList(self, head):
        while head:
            print(head.data, end=" ")
            head = head.next

head = Node(17)
head.next = Node(15)
head.next.next = Node(8)
head.next.next.next = Node(12)
head.next.next.next.next = Node(10)
head.next.next.next.next.next = Node(5)
head.next.next.next.next.next.next = Node(4)
sol = Solution()
newHead = sol.oddEvenList(head)
sol.printList(newHead)
