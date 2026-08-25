'''My brute force'''  
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
# class Solution:
#     def addingOne(self, head):
#         temp = head
#         a = 0
#         while temp:
#             a = a*10 + temp.data
#             temp = temp.next
#         a += 1
#         a = str(a)
#         newhead = Node(a[0])
#         newtail = newhead
#         for i in range(1, len(a)):
#             newtail.next = Node(a[i])
#             newtail = newtail.next
#         return newhead
#     def printLinkedList(self, head):
#         current = head
#         while current:
#             print(current.data,end="->")
#             current = current.next
# if __name__ == "__main__":
#     head = Node(1)
#     head.next = Node(2)
#     head.next.next = Node(3)
#     head.next.next.next = Node(4)
#     head.next.next.next.next = Node(5)
#     sol = Solution()
#     head = sol.addingOne(head)
#     sol.printLinkedList(head)


'''Recursive approach'''
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
# class Solution:
#     def addOneUtil(self, node):
#         if not node:
#             return 1
#         carry = self.addOneUtil(node.next)  
#         total = node.data + carry
#         node.data = total % 10
#         return total // 10
#     def addOne(self, head):
#         carry = self.addOneUtil(head)
#         if carry:
#             new_head = Node(carry)
#             new_head.next = head
#             head = new_head
#         return head
#     def printLinkedList(self, head):
#         current = head
#         while current:
#             print(current.data,end="->")
#             current = current.next
# if __name__ == "__main__":
#     head = Node(1)
#     head.next = Node(2)
#     head.next.next = Node(3)
#     head.next.next.next = Node(4)
#     head.next.next.next.next = Node(5)
#     sol = Solution()
#     head = sol.addOne(head)
#     sol.printLinkedList(head)


'''Iterative approach (Optimal approach)'''
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class Solution:
    def reverseList(self, node):
        prev = None
        current = node
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    def addOne(self, head):
        head = self.reverseList(head)
        current = head
        carry = 1
        while current and carry:
            sum_ = current.data + carry
            current.data = sum_ % 10
            carry = sum_ // 10
            if not current.next and carry:
                current.next = Node(carry)
                carry = 0  
            current = current.next
        head = self.reverseList(head)
        return head
    def printLinkedList(self, head):
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
    sol = Solution()
    head = sol.addOne(head)
    sol.printLinkedList(head)