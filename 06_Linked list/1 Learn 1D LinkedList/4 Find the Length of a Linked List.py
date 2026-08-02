'''My apporach'''
class Node:
    def __init__(self, data1):
        self.data = data1
        self.next = None
class Solution:
    def findingLenth(self, head):
        current = head
        len = 0
        while current:
            len += 1
            current = current.next
        return len
if __name__ == "__main__":

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    a = Solution()
    print(a.findingLenth(head))