class Solution:
    def allPossibleFBT(self, N):
        if not N % 2:
            return []
        cache = collections.defaultdict(list)
        cache[1] = [TreeNode(0)]
        for i in range(3, N + 1, 2):
            for j in range(1, i, 2):
                for lkid in cache[j]:
                    for rkid in cache[i - j - 1]:
                        node = TreeNode(0)
                        node.left = lkid
                        node.right = rkid
                        cache[i].append(node)
        return cache[N]
