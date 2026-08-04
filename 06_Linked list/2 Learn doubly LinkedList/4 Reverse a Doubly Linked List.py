'''Brute force'''
# class Node:
#     def __init__(self, data, next=None, back=None):
#         self.data = data
#         self.next = next
#         self.back = back
# def convertArr2DLL(arr):
#     head = Node(arr[0])
#     prev = head
#     for i in range(1, len(arr)):
#         temp = Node(arr[i], None, prev)
#         prev.next = temp
#         prev = temp
#     return head
# def printDLL(head):
#     while head:
#         print(head.data, end=" ")
#         head = head.next
# def reverseDLL(head):
#     if not head or not head.next:
#         return head
#     stack = []
#     temp = head
#     while temp:
#         stack.append(temp.data)
#         temp = temp.next
#     temp = head
#     while temp:
#         temp.data = stack.pop()
#         temp = temp.next
#     return head

# # Driver code
# arr = [12, 5, 8, 7, 4]
# head = convertArr2DLL(arr)
# print("Doubly Linked List Initially:")
# printDLL(head)
# head = reverseDLL(head)
# print("\nDoubly Linked List After Reversing:")
# printDLL(head)



'''My approach''' # just printing but not converting it
# class Node:
#     def __init__(self, data, next=None, perv=None):
#         self.data = data
#         self.next = next
#         self.perv = perv
# class Solution:
#     def convertarr2DLL(self, arr):
#         head = Node(arr[0])
#         perv = head

#         for i in range(1, len(arr)):
#             temp = Node(arr[i], None, perv)
#             perv.next = temp
#             perv = temp
#         return head
#     def ReverseLL(self, head):
#         current = head
#         while current.next:
#             current = current.next
#         while current:
#             print(current.data, end="->")
#             current = current.perv
# if __name__ == "__main__":
#     arr = [1, 2, 3]
#     a = Solution()
#     head = a.convertarr2DLL(arr)
#     a.ReverseLL(head)



'''simple approach'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
def convert_list_to_dll(arr):
    head = Node(arr[0])
    prev = head
    for i in range(1, len(arr)):
        new_node = Node(arr[i])
        new_node.prev = prev
        prev.next = new_node
        prev = new_node
    return head
def reverse_dll(head):
    temp = None
    current = head
    while current is not None:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev
    if temp is not None:
        head = temp.prev
    return head
def print_dll(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()

# Driver code
if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    head = convert_list_to_dll(arr)
    print("Original DLL:")
    print_dll(head)
    head = reverse_dll(head)
    print("Reversed DLL:")
    print_dll(head)
