# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ans = set()

        def dfs(s, char):
            if not s:
                return
            tmp = char + '->' + str(s.val) if char else str(s.val)
            if s.left is None and s.right is None:
                ans.add(tmp)
            dfs(s.left, tmp)
            dfs(s.right, tmp)
        dfs(root, '')
        return list(ans)
