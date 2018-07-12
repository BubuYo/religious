# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        ans = []
        def helper(node, k):
            if not node or k<0: return
            if k==0: ans.append(node.val)
            helper(node.left, k-1)
            helper(node.right, k-1)
        def dis(node, target, k):
            if node is None: return
            if node == target:
                helper(node, K)
                return 0
            l, r = dis(node.left, target, k), dis(node.right,target,k)
            if l is not None:
                if l == k-1: ans.append(node.val)
                helper(node.right, k-l-2)
                return l+1
            if r is not None:
                if r == k-1: ans.append(node.val)
                helper(node.left, k-l-2)
                return r+1
            return

        dis(root, target, K)
        return ans
                


        