'''Doubly Linked Lists,  as the name suggests, allows 2-way traversal by
introducing two pointers in each node.This enables seamless traversal in both directions,
making them a valuable tool for various advanced data structure applications.'''

class Node:
    def __init__(self, data, next=None, perv=None):
        self.data = data
        self.next = next
        self.per = perv

arr = [1, 3, 5, 6, 7]
y = Node(arr[0])
print(y)
print(y.data)