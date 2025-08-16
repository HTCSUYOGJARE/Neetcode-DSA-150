# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.check_balance = True
        def depth(node):
            if not node or not self.check_balance:
                return 0
            left_node_depth =depth(node.left)
            right_node_depth = depth(node.right)
            if abs(left_node_depth-right_node_depth)>1:
                self.check_balance=False
            return 1 + max(right_node_depth,left_node_depth)
        s=depth(root)
        return self.check_balance