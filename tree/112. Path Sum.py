# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        def dfs(s, current_sum):
            if not s:
                return False
            sum_ = current_sum + s.val
            if sum == sum_ and not s.left and not s.right:
                return True
            elif dfs(s.left, sum_):
                return True
            elif dfs(s.right, sum_):
                return True
            else:
                return False
        return dfs(root, 0)
