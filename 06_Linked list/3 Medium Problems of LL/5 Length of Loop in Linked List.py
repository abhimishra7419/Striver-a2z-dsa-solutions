'''Brute force'''
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
# class Solution:
#     def lenthofloop(self, head):
#         seen = {}
#         temp = head
#         totallenth = 1
#         while temp:
#             if temp in seen:
#                 return totallenth - seen[temp]
#             seen[temp] = totallenth
#             temp = temp.next
#             totallenth += 1
#         return -1
# if __name__ == "__main__":
#     head = Node(1)
#     head.next = Node(2)
#     head.next.next = Node(3)
#     head.next.next.next = Node(4)
#     head.next.next.next.next = head.next

#     a = Solution()
#     print(a.lenthofloop(head))



'''Optimal approach'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class Solution:
    def lenthofloop(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                lenth = 1
                slow = slow.next
                while fast != slow:
                    slow = slow.next
                    lenth += 1
                return lenth
        return -1
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = head.next

    a = Solution()
    print(a.lenthofloop(head))