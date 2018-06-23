# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        levels = set()

        def dfs(s, l):
            if not s:
                return
            if s.left:
                levels.add(l + 1)
                dfs(s.left, l + 1)
            if s.right:
                levels.add(l + 1)
                dfs(s.right, l + 1)
            levels.add(l)
        dfs(root, 1)
        return max(levels)
