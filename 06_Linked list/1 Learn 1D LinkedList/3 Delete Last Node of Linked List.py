'''apporach'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def deletion(self, head):
        if head is None or head.next is None:
            return None
        current = head
        while current.next.next is not None:
            current = current.next
        current.next = None
        return head

    def makinglist(self, head):
        temp = head
        m = []
        while temp:
            m.append(temp.data)
            temp = temp.next
        return m

if __name__ == "__main__":

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    a = Solution()
    head = a.deletion(head)
    print(a.makinglist(head))

