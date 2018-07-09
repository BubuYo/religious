# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        t = []
        def h(node, tmp):
            if node:
                h(node.left, tmp)
                tmp.append(node.val)
                h(node.right, tmp)
        h(root, t)
        return t