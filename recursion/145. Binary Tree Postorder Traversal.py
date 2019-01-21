# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        ans = []
        if root.left != None:
            ans.extend(self.postorderTraversal(root.left))
        if root.right != None:
            ans.extend(self.postorderTraversal(root.right))
        ans.append(root.val)

        return ans
