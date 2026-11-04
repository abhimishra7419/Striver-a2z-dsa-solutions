'''Optimal Solution'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode(-1)
        # 'tail' will track the last node in our merged list
        tail = dummy
        
        # Iterate as long as both lists have nodes remaining
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next  # Move pointer forward in list1
            else:
                tail.next = list2
                list2 = list2.next  # Move pointer forward in list2
            
            tail = tail.next  # Move the merged list tail forward
            
        # If one list is exhausted, append the remaining elements of the other list
        tail.next = list1 if list1 else list2
        
        # Return the actual head, skipping the dummy node
        return dummy.next