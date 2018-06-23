# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(p, q):
            if not all([p, q]):
                return p == q
            return p.val == q.val and check(p.left, q.right) and check(p.right, q.left)
        return check(root, root)
