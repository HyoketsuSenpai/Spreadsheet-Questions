# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def eq(n1,n2):
            if not n1 and n2:
                return False
            if n1 and not n2:
                return False
            if n1 and n2:
                if n1.val != n2.val:
                    return False
                return eq(n1.left,n2.left) and eq(n1.right, n2.right)
            return True
        return eq(q,p)
