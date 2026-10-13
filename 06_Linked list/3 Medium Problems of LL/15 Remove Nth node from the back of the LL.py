'''My approach'''
class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class Solution:
    def LL(self, arr, n):
        head = ListNode(arr[0])
        temp = head
        for i in range(1, len(arr)):
            temp.next = ListNode(arr[i])
            temp = temp.next
        head = self.Removing(head, n)
        temp = head
        arr = []
        while temp:
            arr.append(temp.data)
            temp = temp.next
        print("None")
        return arr

    def Removing(self, head, n):
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        position = length - n
        if position == 0:
            return head.next
        temp = head
        for _ in range(position - 1):
            temp = temp.next
        temp.next = temp.next.next
        return head

if __name__ == "__main__":
    head = [1,2,3,4,5]
    n = 1
    a = Solution()
    print(a.LL(head, n))