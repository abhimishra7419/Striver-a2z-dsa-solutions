'''Optimal approach'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class Solution:
    def getKthNode(self, head, k):
        current = head
        while current and k>0:
            current = current.next
            k -= 1
        return current
    def reverseLL(self, head, k):
        dummy = Node(-1)
        dummy.next = head
        groupPrev = dummy

        while True:
            Kth = self.getKthNode(groupPrev, k)
            if not Kth:
                break
            groupNext = Kth.next

            prev = groupNext
            curr = groupPrev.next

            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            temp = groupPrev.next
            groupPrev.next = Kth
            groupPrev = temp


            head = groupNext
        return dummy.next
            

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
    newhead = a.reverseLL(head, 2)
    a.printLL(newhead)
