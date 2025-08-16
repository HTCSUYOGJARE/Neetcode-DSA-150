# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.check_balance = set()
        def depth(node):
            if not node:
                return 0
            left_node_depth =depth(node.left)
            right_node_depth = depth(node.right)
            self.check_balance.add(abs(left_node_depth-right_node_depth)<=1)
            return 1 + max(right_node_depth,left_node_depth)
        s=depth(root)
        return False if False in self.check_balance else True