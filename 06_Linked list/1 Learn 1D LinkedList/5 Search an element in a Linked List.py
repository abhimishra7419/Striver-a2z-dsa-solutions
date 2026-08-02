'''My approach'''
class Node:
    def __init__(self, data1):
        self.data = data1
        self.next = None
class Solution:
    def searching(self, head, target):
        current = head
        while current:
            if current.data == target:
                return True
            current = current.next
        return False

if __name__ == "__main__":

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    target = 3
    a = Solution()
    print(a.searching(head, target))