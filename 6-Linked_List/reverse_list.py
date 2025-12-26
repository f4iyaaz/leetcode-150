# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        if head.next is None:
            return head
        prev = None
        curr = head
        while curr.next is not None:
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
            # print(curr.val)
        curr.next = prev
        head = curr
        self.head = head
        return self.head

  # Beats 100% of runtimes
