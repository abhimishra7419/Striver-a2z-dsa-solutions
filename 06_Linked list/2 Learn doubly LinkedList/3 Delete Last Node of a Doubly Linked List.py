'''My approach'''
class Node:
    def __init__(self, data, next=None, perv=None):
        self.data = data
        self.next = next
        self.perv = perv
class Solution():
    def convertarr2DLL(self, arr):
        head = Node(arr[0])
        perv = head
        for i in range(1, len(arr)):
            temp = Node(arr[i], None, perv)
            perv.next = temp
            perv = temp
        return head
    def deletion(self, head):
        if not head:
            return None
        current = head
        while current:
            if current.next.next == None:
                current.next = None
            current = current.next
        return head
    def printlist(self, head):
        current = head
        while current:
            print(current.data, end="->")
            current = current.next
if __name__ == "__main__":
    arr = [1, 2, 3]
    a = Solution()
    head = a.convertarr2DLL(arr)
    head = a.deletion(head)
    a.printlist(head)


'''Simple approach'''
# Node structure for DLL
class Node:
    def __init__(self, val):
        self.data = val
        self.prev = None
        self.next = None

class Solution:
    def deleteTail(self, head):
        if not head:
            return None
        if not head.next:
            return None
        temp = head
        while temp.next:
            temp = temp.next
        temp.prev.next = None
        return head

# Driver code
if __name__ == "__main__":
    # Create a sample DLL: 1 <-> 2 <-> 3
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next

    obj = Solution()
    head = obj.deleteTail(head)

    # Print list after deletion
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
