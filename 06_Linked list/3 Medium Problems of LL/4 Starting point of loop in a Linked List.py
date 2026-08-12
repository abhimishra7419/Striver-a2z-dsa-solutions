'''approach'''
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
# class Solution:
#     def finding(self, head):
#         nodemap = set()
#         temp = head
#         while temp:
#             if temp in nodemap:
#                 return temp.data
#             nodemap.add(temp)
#             temp = temp.next
#         return None
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
#     fifth.next = third

#     a = Solution()
#     print(a.finding(head))


'''Optimal approach'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class Solution:
    def finding(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow.data
        return None
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
    fifth.next = third

    a = Solution()
    print(a.finding(head))
