'''My approach'''
class Node:
    def __init__(self, data, next=None, perv=None):
        self.data = data
        self.next = next
        self.perv = perv

class Solution:
    def inserting(self, head, element):
        current = head
        while current:
            if current.next is None:
                current.next = Node(element)
                perv_reference = current
            current = current.next
        current.prev = perv_reference

    def printList(self, head):
        current = head
        while current:
            print(current.data, end="->")
            current = current.next

if __name__ == "__main__":

    head = Node(1)
    head.next = Node(2)
    head.next.perv = Node(1)
    head.next.next = Node(3)
    head.next.next.perv = Node(2)

    a = Solution()
    print("Current LinkedList: ",end="")
    a.printList(head)

    a.inserting(head, 4)

    print("After inserting: ",end="")
    a.printList(head)