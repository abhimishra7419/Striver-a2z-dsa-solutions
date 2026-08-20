'''brute force'''
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
# class Solution:
#     def removingNode(self, head, N):
#         if not head:
#             return None
#         marker = 0
#         current = head
#         while current:
#             marker += 1
#             current = current.next
#         if marker == N:
#             return head.next
#         res = marker - N
#         temp = head
#         while temp:
#             res -= 1
#             if res == 0:
#                 break
#             temp = temp.next
#         temp.next = temp.next.next
#         return head

#     def printlist(self, head):
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
#     N = 2
#     a = Solution()
#     newhead = a.removingNode(head, N)
#     a.printlist(newhead)


'''My Optimal approach'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class Solution():
    def removingNode(self, head, N):
        # dummy = Node(0, head)
        # slow = dummy
        # fast = dummy
        slow = head
        fast = head
        for _ in range(N+1):
            fast = fast.next
        while fast is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        # return dummy.next
        return head
    def printlist(self, head):
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
    N = 2
    a = Solution()
    newhead = a.removingNode(head, N)
    a.printlist(newhead)

