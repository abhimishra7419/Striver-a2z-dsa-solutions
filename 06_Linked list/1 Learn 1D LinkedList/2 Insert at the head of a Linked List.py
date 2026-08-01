'''approach'''
class Node:
    def __init__(self, data1, Next1=None):
        self.data = data1
        self.Next = Next1
class Solution:
    def inserting(self, head, newitem):
        newNode = Node(newitem, head)
        return newNode
    def printlist(self, head):
        temp = head
        while temp:
            print(temp.data, end=" ")
            temp = temp.Next
        print()

if __name__ == "__main__":
    a = Solution()

    head = Node(2)
    head.Next = Node(3)

    print("Orignal list:", end="")
    a.printlist(head)

    head = a.inserting(head, 1)

    print("New list:", end="")
    a.printlist(head)
