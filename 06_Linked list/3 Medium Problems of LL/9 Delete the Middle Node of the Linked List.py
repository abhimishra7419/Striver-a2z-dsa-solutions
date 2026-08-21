'''My Optimal approach'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class Solution:
    def DeletingMiddle(self, head):
        if head is None or head.next is None:
            return None
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return slow.next.data
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
    newhead = a.DeletingMiddle(head)
    a.printLL(newhead)
