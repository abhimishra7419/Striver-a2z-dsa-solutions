'''Brute force'''
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
# class Solution:
#     def sorting(self, head):
#         arr = []
#         current = head
#         while current:
#             arr.append(current.data)
#             current = current.next
#         arr.sort()
#         temp = head
#         for i in arr:
#             temp.data = i
#             temp = temp.next
#         return head
#     def printLL(self, head):
#         current = head
#         while current:
#             print(current.data,end="->")
#             current = current.next
# if __name__ == "__main__":
#     head = Node(5)
#     head.next = Node(4)
#     head.next.next = Node(3)
#     head.next.next.next = Node(4)
#     head.next.next.next.next = Node(1)
#     a = Solution()
#     newhead = a.sorting(head)
#     a.printLL(newhead)

'''Optimal approach'''
class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1
class Solution:
    def mergeTwoSortedLinkedLists(self, list1, list2):
        dummyNode = Node(-1)
        temp = dummyNode
        while list1 and list2:
            if list1.data <= list2.data:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        if list1:
            temp.next = list1
        else:
            temp.next = list2
        return dummyNode.next
    def findMiddle(self, head):
        # If list empty or single node
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def sortLL(self, head):
        if not head or not head.next:
            return head
        middle = self.findMiddle(head)
        right = middle.next
        middle.next = None
        left = head
        left = self.sortLL(left)
        right = self.sortLL(right)
        return self.mergeTwoSortedLinkedLists(left, right)
def printLinkedList(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()
if __name__ == "__main__":
    # Create linked list: 3 -> 2 -> 5 -> 4 -> 1
    head = Node(3)
    head.next = Node(2)
    head.next.next = Node(5)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(1)
    print("Original Linked List:", end=" ")
    printLinkedList(head)
    obj = Solution()
    head = obj.sortLL(head)
    print("Sorted Linked List:", end=" ")
    printLinkedList(head)