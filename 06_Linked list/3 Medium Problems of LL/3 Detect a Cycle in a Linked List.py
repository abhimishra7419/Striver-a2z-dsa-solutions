'''approach'''
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
# class Solution:
#     def detecting(self, head):
#         temp = head
#         nodemap = {}

#         while temp:
#             if temp in nodemap:
#                 return True
#             nodemap[temp] = 1
#             temp = temp.next
#         return False
# if __name__ == "__main__":
#     head = Node(1)
#     second = Node(2)
#     third = Node(3)
#     fourth = Node(4)
#     fifth = Node(5)

#     head.next = second
#     second.next = third
#     third.next = fourth
#     fourth.next = fifth
#     # Create a loop
#     fifth.next = fifth

#     a = Solution()
#     print(a.detecting(head))



'''Optimal approach'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class Solution:
    def detecting(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

if __name__ == "__main__":
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    # Create a loop
    fifth.next = fifth

    a = Solution()
    print(a.detecting(head))
