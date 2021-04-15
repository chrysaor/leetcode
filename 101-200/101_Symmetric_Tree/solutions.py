# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @classmethod
    def is_symmetric(cls, root: TreeNode) -> bool:
        if root.left is None and root.right is None:
            return True

        left_r = root
        right_r = root

        while True:
            pass
