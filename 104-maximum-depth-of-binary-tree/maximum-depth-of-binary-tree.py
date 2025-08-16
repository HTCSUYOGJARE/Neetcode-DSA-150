# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res=0
        if not root:
            return res
        res+=1
        l=self.maxDepth(root.left)
        r=self.maxDepth(root.right)
        return max(res+l,res+r)
