# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None and q is not None:
            return False
        if p is not None and q is None:
            return False
        q1 = deque()
        q2 = deque()
        l1 = []
        l2 = []
        q1.append(p)
        q2.append(q)
        l1.append(p.val)
        l2.append(q.val)
        while q1 and q2:
            q1_node = q1.popleft()
            q2_node = q2.popleft()

            if q1_node.left:
                q1.append(q1_node.left)
                l1.append(q1_node.left.val)
            else:
                l1.append(None)
            if q1_node.right:
                q1.append(q1_node.right)
                l1.append(q1_node.right.val)
            else:
                l1.append(None)
            if q2_node.left:
                q2.append(q2_node.left)
                l2.append(q2_node.left.val)
            else:
                l2.append(None)
            if q2_node.right:
                q2.append(q2_node.right)
                l2.append(q2_node.right.val)
            else:
                l2.append(None)
    
        if l1 == l2:
            return True
        else:
            return False


# Runtime: Beats 100%
