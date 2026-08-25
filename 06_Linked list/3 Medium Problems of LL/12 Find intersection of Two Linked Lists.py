'''Brute force'''
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
# class Solution:
#     def intersection(self, head1, head2):
#         temp = head2
#         while temp:
#             current = head1
#             while current:
#                 if current == temp:
#                     return temp
#                 current = current.next
#             temp =  temp.next
#         return None
#     def printLinkedList(self, head):
#         current = head
#         while current:
#             print(current.data,end="->")
#             current = current.next
# if __name__ == "__main__":
#     head = Node(1)
#     head.next = Node(2)
#     head.next.next = Node(3)
#     head.next.next.next = Node(4)
#     head.next.next.next.next = Node(5)
#     head2 = Node(6)
#     head2.next = Node(7)
#     head2.next.next = Node(8)
#     head2.next.next.next = head
#     head2.next.next.next.next = head.next
#     sol = Solution()
#     head = sol.intersection(head, head2)
#     sol.printLinkedList(head)


'''Better approach'''
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
# class Solution:
#     def intersection(self, head, head2):
#         st = set()
#         temp = head
#         while temp:
#             st.add(temp)
#             temp = temp.next
#         current = head2
#         while current:
#             if current in st:
#                 return current
#             current = current.next
#         return None
#     def printLinkedList(self, head):
#         current = head
#         while current:
#             print(current.data,end="->")
#             current = current.next
# if __name__ == "__main__":
#     head = Node(1)
#     head.next = Node(2)
#     head.next.next = Node(3)
#     head.next.next.next = Node(4)
#     head.next.next.next.next = Node(5)
#     head2 = Node(6)
#     head2.next = Node(7)
#     head2.next.next = Node(8)
#     head2.next.next.next = head
#     head2.next.next.next.next = head.next
#     sol = Solution()
#     head = sol.intersection(head, head2)
#     sol.printLinkedList(head)



'''Optimal approach'''
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
# class Solution:
#     def difference(self, head, head2):
#         temp = head
#         temp2 = head2
#         count, count2 = 0, 0
#         while temp or temp2:
#             if temp:
#                 count += 1
#                 temp = temp.next
#             if temp2:
#                 count2 += 1
#                 temp2 = temp2.next
#         return count - count2
#     def intersection(self, head, head2):
#         diff = self.difference(head, head2)
#         temp = head
#         temp2 = head2
#         if diff < 0:
#             for _ in range(abs(diff)):
#                 temp2 = temp2.next
#         else:
#             for _ in range(diff):
#                 temp = temp.next
#         while temp:
#             if temp == temp2:
#                 return temp
#             temp = temp.next
#             temp2 = temp2.next
#         return None
#     def printLinkedList(self, head):
#         current = head
#         while current:
#             print(current.data,end="->")
#             current = current.next
# if __name__ == "__main__":
#     head = Node(1)
#     head.next = Node(2)
#     head.next.next = Node(3)
#     head.next.next.next = Node(4)
#     head.next.next.next.next = Node(5)
#     head2 = Node(6)
#     head2.next = Node(7)
#     head2.next.next = Node(8)
#     head2.next.next.next = head
#     head2.next.next.next.next = head.next
#     sol = Solution()
#     head = sol.intersection(head, head2)
#     sol.printLinkedList(head)


'''Optimal approach 2'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class Solution:
    def intersection(self, head, head2):
        d1, d2 = head, head2
        while d1 != d2:
            d1 = head2 if d1 is None else d1.next
            d2 = head if d2 is None else d2.next
        return d1
    def printLinkedList(self, head):
        current = head
        while current:
            print(current.data,end="->")
            current = current.next
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head2 = Node(6)
    head2.next = Node(7)
    head2.next.next = Node(8)
    head2.next.next.next = head
    head2.next.next.next.next = head.next
    sol = Solution()
    head = sol.intersection(head, head2)
    sol.printLinkedList(head)