'''My approach'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class Solution:
    def reverseLL(self, head, k):
        current = head
        if k == 0:
            return head
        prev = current
        current = current.next
        k -= 1
        while k:
            next = current.next
            current.next = head
            head.next = next
            current.next = prev
            prev = current
            current = next
            k -= 1
        return prev
    def printLL(self, head):
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
    a = Solution()
    newhead = a.reverseLL(head, 4)
    a.printLL(newhead)