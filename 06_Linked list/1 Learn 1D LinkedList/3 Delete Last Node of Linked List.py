'''My apporach'''
class Node:
    def __init__(self, data):
        self.data = data
        self.Next = None

class Solution:
    def deletion(self, head):
        if head is None or head.next is None:
            return None