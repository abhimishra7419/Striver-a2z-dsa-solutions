'''brute force'''
# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.next = None
#         self.random = None
# def insertCopyInBetween(head):
#     temp = head
#     while temp:
#         nextElement = temp.next
#         copy = Node(temp.data)
#         copy.next = nextElement
#         temp.next = copy
#         temp = nextElement
# def connectRandomPointers(head):
#     temp = head
#     while temp:
#         copyNode = temp.next
#         if temp.random:
#             copyNode.random = temp.random.next
#         else:
#             copyNode.random = None
#         temp = temp.next.next
# def getDeepCopyList(head):
#     temp = head
#     dummyNode = Node(-1)
#     res = dummyNode
#     while temp:
#         res.next = temp.next
#         res = res.next
#         temp.next = temp.next.next
#         temp = temp.next
#     return dummyNode.next
# def cloneLL(head):
#     if not head:
#         return None
#     insertCopyInBetween(head)
#     connectRandomPointers(head)
#     return getDeepCopyList(head)
# def printClonedLinkedList(head):
#     while head:
#         print("Data:", head.data, end="")
#         if head.random:
#             print(", Random:", head.random.data, end="")
#         else:
#             print(", Random: None", end="")
#         print()
#         head = head.next

# # Main function
# if __name__ == "__main__":
#     # Example linked list: 7 -> 14 -> 21 -> 28
#     head = Node(7)
#     head.next = Node(14)
#     head.next.next = Node(21)
#     head.next.next.next = Node(28)

#     head.random = head.next.next
#     head.next.random = head
#     head.next.next.random = head.next.next.next
#     head.next.next.next.random = head.next

#     clonedList = cloneLL(head)

#     print("\nCloned Linked List with Random Pointers:")
#     printClonedLinkedList(clonedList)


'''Optimal approach'''
class Node:
    # Data stored in the node
    def __init__(self, x):
        self.data = x
        self.next = None
        self.random = None
class Solution:
    def insertCopyInBetween(self, head):
        temp = head
        while temp:
            nextElement = temp.next
            copy = Node(temp.data)
            copy.next = nextElement
            temp.next = copy
            temp = nextElement
    def connectRandomPointers(self, head):
        temp = head
        while temp:
            copyNode = temp.next
            if temp.random:
                copyNode.random = temp.random.next
            else:
                copyNode.random = None

            temp = temp.next.next

    def getDeepCopyList(self, head):
        temp = head
        dummyNode = Node(-1)
        res = dummyNode

        while temp:
            res.next = temp.next
            res = res.next

            temp.next = temp.next.next
            temp = temp.next

        return dummyNode.next

    def cloneLL(self, head):
        if not head:
            return None

        self.insertCopyInBetween(head)
        self.connectRandomPointers(head)
        return self.getDeepCopyList(head)
    def printClonedLinkedList(self, head):
        while head:
            print("Data:", head.data, end="")
            if head.random:
                print(", Random:", head.random.data, end="")
            else:
                print(", Random: None", end="")
            print()
            head = head.next

# Main function
if __name__ == "__main__":
    # Example linked list: 7 -> 14 -> 21 -> 28
    head = Node(7)
    head.next = Node(14)
    head.next.next = Node(21)
    head.next.next.next = Node(28)

    head.random = head.next.next
    head.next.random = head
    head.next.next.random = head.next.next.next
    head.next.next.next.random = head.next
    a = Solution()

    clonedList = a.cloneLL(head)

    print("\nCloned Linked List with Random Pointers:")
    a.printClonedLinkedList(clonedList)
