'''Brute force'''
# class Node:
#     def __init__(self, data, prev=None, next=None):
#         self.data = data
#         self.prev = prev
#         self.next = next
# class Solution:
#     def convertinginDLL(self, arr):
#         head = Node(arr[0])
#         prev = head
#         for i in range(1, len(arr)):
#             temp = Node(arr[i], prev, None)
#             prev.next = temp
#             prev = temp
#         return head
#     def findingallpairs(self, head, target):
#         temp1 = head
#         pairs = []
#         while temp1:
#             temp2 = temp1.next
#             while temp2:
#                 if temp1.data + temp2.data == target:
#                     pairs.append((temp1.data, temp2.data))
#                     break
#                 elif temp1.data + temp2.data < target:
#                     temp2 = temp2.next
#                 else:
#                     break
#             temp1 = temp1.next
#         return pairs
# if __name__ == "__main__":
#     arr = [1, 2, 3, 4, 5, 6, 7, 8]
#     a = Solution()
#     target = 8
#     head = a.convertinginDLL(arr)
#     print(a.findingallpairs(head, target))


'''Optimal Solution'''
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
    def findingallpairs(self, head, target):
        left = head
        right = head
        pairs = []
        while right.next:
            right = right.next

        
        while left.data < right.data:
            if left.data + right.data == target:
                pairs.append((left.data, right.data))
                left = left.next
                right = right.prev
            elif left.data + right.data > target:
                right = right.prev
            else:
                left = left.next
        return pairs
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    a = Solution()
    target = 5
    head = a.convertinginDLL(arr)
    print(a.findingallpairs(head, target))