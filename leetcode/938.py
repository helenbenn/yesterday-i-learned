# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return 0

        v = 0
        if L <= root.val <= R:
            v = root.val

        l_sum = self.rangeSumBST(root.left, L, R)
        r_sum = self.rangeSumBST(root.right, L, R)
        return v + l_sum + r_sum