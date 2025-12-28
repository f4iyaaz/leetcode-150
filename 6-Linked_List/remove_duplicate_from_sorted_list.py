# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return head
        left = head
        right = head.next
        while right.next is not None:
            if left.val != right.val:
                left.next = right
                left = right
                right = right.next
            else:
                right = right.next

        if left.val != right.val:
            left.next = right
        else:
            left.next = None

        return head
        
# Runtime: Beats 100%
