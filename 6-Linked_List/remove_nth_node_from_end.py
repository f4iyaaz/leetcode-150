# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        ahead = dummy
        behind = dummy
        flag = False
        for _ in range(n + 1):
            ahead = ahead.next
        while ahead:
            flag = True
            behind = behind.next
            ahead = ahead.next
        if flag:
            behind.next = behind.next.next
            return head
        else:
            dummy.next = dummy.next.next
            head = dummy.next
            return head


# Runtime: Beats 100%
# Memory: Beats 88.42%
