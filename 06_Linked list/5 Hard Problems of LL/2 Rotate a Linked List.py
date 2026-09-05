'''My approach'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class Solution:
    def rotating(self, head, k):
        lastNode = head
        len = 1
        while lastNode.next:
            lastNode = lastNode.next
            len += 1
        k = k % len
        if k == 0:
            return head
        lastNode.next = head
        newtail = head
        counter = len-k
        for _ in range(counter-1):
            newtail = newtail.next
        newhead = newtail.next
        newtail.next = None
        return newhead
    def printLL(self, head):
        current = head
        while current:
            print(current.data,end="->")
            current = current.next
if __name__ == "__main__":
    head = Node(0)
    head.next = Node(1)
    head.next.next = Node(2)
    # head.next.next.next = Node(4)
    # head.next.next.next.next = Node(5)
    a = Solution()
    newhead = a.rotating(head, 4)
    a.printLL(newhead)
