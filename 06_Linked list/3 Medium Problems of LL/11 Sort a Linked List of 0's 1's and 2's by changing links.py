'''brute force'''
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
# class Solution:
#     def sortingLL(self, head):
#         count0 = 0
#         count1 = 0
#         count2 = 0
#         current = head
#         while current:
#             if current.data == 0:
#                 count0 += 1
#             elif current.data == 1:
#                 count1 += 1
#             else:
#                 count2 += 1
#             current = current.next
#         current = head
#         while count0 != 0:
#             current.data = 0
#             count0 -= 1
#             current = current.next
#         while count1 != 0:
#             current.data = 1
#             count1 -= 1
#             current = current.next
#         while count2 != 0:
#             current.data = 2
#             count2 -= 1
#             current = current.next
#         return head
#     def printLinkedList(self, head):
#         temp = head
#         while temp:
#             print(temp.data, end=" ")
#             temp = temp.next
# if __name__ == "__main__":
#     # Create linked list: 3 -> 2 -> 5 -> 4 -> 1
#     head = Node(1)
#     head.next = Node(2)
#     head.next.next = Node(0)
#     head.next.next.next = Node(1)
#     head.next.next.next.next = Node(0)
#     a = Solution()
#     print("Original Linked List:", end=" ")
#     a.printLinkedList(head)
#     head = a.sortingLL(head)
#     print("Sorted Linked List:", end=" ")
#     a.printLinkedList(head)


'''Optimal Solution'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
class Solution:
    def sortZeroOneTwo(self, head):
        zero_dummy = Node(-1)
        one_dummy = Node(-1)
        two_dummy = Node(-1)
        zero_tail = zero_dummy
        one_tail = one_dummy
        two_tail = two_dummy
        curr = head
        while curr:
            if curr.data == 0:
                zero_tail.next = curr
                zero_tail = zero_tail.next
            elif curr.data == 1:
                one_tail.next = curr
                one_tail = one_tail.next
            else:
                two_tail.next = curr
                two_tail = two_tail.next
            curr = curr.next
        zero_tail.next = one_dummy.next if one_dummy.next else two_dummy.next
        one_tail.next = two_dummy.next
        two_tail.next = None
        return zero_dummy.next

    def printLinkedList(self, head):
        temp = head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next        
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(0)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(0)
    sol = Solution()
    head = sol.sortZeroOneTwo(head)
    sol.printLinkedList(head)