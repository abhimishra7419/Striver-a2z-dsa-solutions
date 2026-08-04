'''Approach'''
class Node:
    def __init__(self, data, next=None, perv=None):
        self.data = data
        self.next = next
        self.perv = perv
class Solution:
    def convertarray2DLL(self, arr):
        head = Node(arr[0])
        perv = head
        for i in range(1, len(arr)):
            temp = Node(arr[i], None, perv)
            perv.next = temp
            perv = temp
        return head
    def printList(self, head):
        current = head
        while current:
            print(current.data, end="->")
            current = current.next
    def inseting(self, head, k):
        newNode = Node(k)
        tail = head
        while tail.next:
            tail = tail.next
        tail.next = newNode
        newNode.prev = tail    #adding pointer in last node
        return tail

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    a = Solution()
    head = a.convertarray2DLL(arr)
    head = a.inseting(head, 7)
    a.printList(head)