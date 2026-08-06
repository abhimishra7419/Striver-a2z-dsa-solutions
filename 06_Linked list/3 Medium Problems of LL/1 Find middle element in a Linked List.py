'''My approach'''
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
# class Solution:
#     def lenth(self, head):
#         len = 0
#         current = head
#         while current:
#             len += 1
#             current = current.next
#         return len
#     def middle(self, head, len):
#         if len == 0:
#             return -1
#         mid = len//2
#         current = head
#         for _ in range(mid):
#             current = current.next
#         return current.data
# if __name__ == "__main__":
#     head = Node(0)
#     head.next = Node(1)
#     head.next.next = Node(2)
#     head.next.next.next = Node(3)
#     head.next.next.next.next = Node(4)
#     head.next.next.next.next.next = Node(5)
#     a = Solution()
#     len = a.lenth(head)
#     print(a.middle(head, len))


'''Brute force'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    