# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        mins = []

        def dfs(p, level):
            if not p:
                return
            if not p.left and not p.right:
                mins.append(level)
            if p.left:
                dfs(p.left, level+1)
            if p.right:
                dfs(p.right, level+1)
        dfs(root, 1)
        return min(mins)
