# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution:
    def __init__(self):
        self._dict = collections.defaultdict(int)

    def find(self, node):
        if node:
            self._dict[node.val] += 1
            self.find(node.left)
            self.find(node.right)

    def findMode(self, root: TreeNode) -> List[int]:
        self.find(root)
        max_count, ans = 0, []
        for num, count in self._dict.items():
            if count == max_count:
                ans.append(num)
            elif count > max_count:
                ans = [num]
                max_count = count
        return ans
