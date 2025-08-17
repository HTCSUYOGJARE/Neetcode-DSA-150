# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
                #Its a BST so check p and q with root
        if (p.val<=root.val and q.val>=root.val) or (p.val>=root.val and q.val<=root.val):
            return root
        if p.val<root.val and q.val<root.val: # if bot p and q are lesser than root then search in left of root only
            return self.lowestCommonAncestor(root.left,p,q)
        else: # when both p.val and q.val are greater than root.val so search in right side of root as its a BST
            return self.lowestCommonAncestor(root.right,p,q)