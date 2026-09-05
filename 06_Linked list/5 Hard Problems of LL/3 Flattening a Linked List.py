'''My brute force'''
# class Node:
#     def __init__(self, data, child=None, next=None):
#         self.data = data
#         self.child = child
#         self.next = next
# class Solution:
#     def flattening(self, head):
#         if not head:
#             return None
#         current = head
#         while current:
#             if current.child:
#                 childtail = current.child
#                 while childtail.next:
#                     childtail = childtail.next
#                 childtail.next = current.next
#                 current.next = current.child
#                 current.child = None
#             current = current.next
#         return head
#     def sorting(self, head):
#         arr = []
#         current = head
#         while current:
#             arr.append(current.data)
#             current = current.next
#         arr.sort()
#         newhead = Node(arr[0])
#         current = newhead
#         for i in range(1, len(arr)):
#             current.next = Node(arr[i])
#             current = current.next
#         current.next = None
#         return newhead
#     def printLL(self, head):
#         current = head
#         while current:
#             print(current.data, end="->")
#             current = current.next
# if __name__ == "__main__":
#     # Create a linked list with child pointers
#     head = Node(5)
#     head.child = Node(14)

#     head.next = Node(10)
#     head.next.child = Node(4)

#     head.next.next = Node(12)
#     head.next.next.child = Node(20)
#     head.next.next.child.child = Node(13)

#     head.next.next.next = Node(7)
#     head.next.next.next.child = Node(17)
#     a = Solution()
#     newhead = a.flattening(head)
#     newhead = a.sorting(newhead)
#     a.printLL(newhead)


'''My better approach'''
# class Node:
#     def __init__(self, data, child=None, next=None):
#         self.data = data
#         self.child = child
#         self.next = next
# class Solution:
#     def mergeTwoSortedLinkedLists(self, list1, list2):
#         dummyNode = Node(-1)
#         temp = dummyNode
#         while list1 and list2:
#             if list1.data <= list2.data:
#                 temp.next = list1
#                 list1 = list1.next
#             else:
#                 temp.next = list2
#                 list2 = list2.next
#             temp = temp.next
#         if list1:
#             temp.next = list1
#         else:
#             temp.next = list2
#         return dummyNode.next
#     def findMiddle(self, head):
#         if not head or not head.next:
#             return head
#         slow = head
#         fast = head.next
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         return slow
#     def sortLL(self, head):
#         if not head or not head.next:
#             return head
#         middle = self.findMiddle(head)
#         right = middle.next
#         middle.next = None
#         left = head
#         left = self.sortLL(left)
#         right = self.sortLL(right)
#         return self.mergeTwoSortedLinkedLists(left, right)

#     def flattening(self, head):
#         if not head:
#             return None
#         current = head
#         while current:
#             if current.child:
#                 current.child = self.sortLL(current.child)
#                 childtail = current.child
#                 while childtail.next:
#                     childtail = childtail.next
#                 childtail.next = current.next
#                 current.next = current.child
#                 current.child = None
#             current = current.next
#         newhead = self.sortLL(head)
#         return newhead
#     def printLL(self, head):
#         current = head
#         while current:
#             print(current.data, end="->")
#             current = current.next
# if __name__ == "__main__":
#     # Create a linked list with child pointers
#     head = Node(5)
#     head.child = Node(14)
#     head.next = Node(10)
#     head.next.child = Node(4)
#     head.next.next = Node(12)
#     head.next.next.child = Node(20)
#     head.next.next.child.child = Node(13)
#     head.next.next.next = Node(7)
#     head.next.next.next.child = Node(17)
#     a = Solution()
#     newhead = a.flattening(head)
#     a.printLL(newhead)

'''Optimal approach'''
class ListNode:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

class Solution:
    def merge(self, list1, list2):
        dummyNode = ListNode(-1)
        res = dummyNode
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                res.child = list1
                res = list1
                list1 = list1.child
            else:
                res.child = list2
                res = list2
                list2 = list2.child
            res.next = None
        if list1:
            res.child = list1
        else:
            res.child = list2
        if dummyNode.child:
            dummyNode.child.next = None

        return dummyNode.child
    def flattenLinkedList(self, head):
        if head is None or head.next is None:
            return head
        mergedHead = self.flattenLinkedList(head.next)
        head = self.merge(head, mergedHead)
        return head
def printLinkedList(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.child
    print()
    
if __name__ == "__main__":
    # Create a linked list with child pointers
    head = ListNode(5)
    head.child = ListNode(14)

    head.next = ListNode(10)
    head.next.child = ListNode(4)

    head.next.next = ListNode(12)
    head.next.next.child = ListNode(20)
    head.next.next.child.child = ListNode(13)

    head.next.next.next = ListNode(7)
    head.next.next.next.child = ListNode(17)

    sol = Solution()

    flattened = sol.flattenLinkedList(head)
    
    print("\nFlattened linked list: ", end="")
    printLinkedList(flattened)