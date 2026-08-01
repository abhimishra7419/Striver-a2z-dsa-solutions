'''
There is 3 types of likedlist :-
1.) singly linkedlist
2.) doubly linkedlist
3.) circular linked
'''

'''Finding address and finding value on address'''
class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
arr = [1, 3, 4, 5, 6]
y = node(arr[1])
y1 = node(1)
print(y)
print(y1)
print(y.data)
print(y1.data)