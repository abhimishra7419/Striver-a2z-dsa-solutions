'''approach'''
class ListNode:
    def __init__(self, data, next=None):
        self.val = data
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        temp = dummy
        carry = 0
        while (l1 is not None or l2 is not None) or carry:
            sum_val = 0
            if l1 is not None:
                sum_val += l1.val
                l1 = l1.next
            if l2 is not None:
                sum_val += l2.val
                l2 = l2.next
            sum_val += carry
            carry = sum_val // 10
            node = ListNode(sum_val % 10)
            temp.next = node
            temp = temp.next
        return dummy.next
def create_list(arr):
    head = ListNode(arr[0])
    temp = head
    for i in arr[1:]:
        temp.next = ListNode(i)
        temp = temp.next
    return head

def print_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next
if __name__ == "__main__":
    num1 = [2, 4, 3]
    num2 = [5, 6, 4]
    l1 = create_list(num1)
    l2 = create_list(num2)

    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)
    print_list(result)  # Output: 7 -> 0 -> 8