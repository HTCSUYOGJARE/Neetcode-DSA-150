# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia=0
        def depth(node):
            if not node:
                return 0
            left_node_depth=depth(node.left)
            right_node_depth = depth(node.right)
            self.dia = max(self.dia,left_node_depth+right_node_depth )
            return 1+max(left_node_depth,right_node_depth )
        s=depth(root)
        return self.dia
        