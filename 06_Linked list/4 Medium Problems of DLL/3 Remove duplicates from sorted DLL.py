'''My Optimal approach'''
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
class Solution:
    def convertinginDLL(self, arr):
        head = Node(arr[0])
        prev = head
        for i in range(1, len(arr)):
            temp = Node(arr[i], prev, None)
            prev.next = temp
            prev = temp
        return head
    def removingDuplicates(self, head):
        current = head
        while current:
            if current.prev and current.prev.data == current.data:
                current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                current = current.next
            else:
                current = current.next
        return head
    def printDLL(self, head):
        current = head
        while current:
            print(current.data,end="<->")
            current = current.next
if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8]
    a = Solution()
    target = 8
    head = a.convertinginDLL(arr)
    newhead = a.removingDuplicates(head)
    a.printDLL(newhead)