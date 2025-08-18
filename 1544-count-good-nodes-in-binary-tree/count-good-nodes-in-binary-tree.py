# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count=1
        def DFS(node,min_val):
            if not node:
                return
            if node.left and node.left.val>=min_val:
                self.count+=1
                DFS(node.left,node.left.val)
            elif node.left and node.left.val<min_val:
                DFS(node.left,min_val)
            if node.right and node.right.val>=min_val:
                self.count+=1
                DFS(node.right,node.right.val)
            elif node.right and node.right.val<min_val:
                DFS(node.right,min_val)
            return
        DFS(root,root.val)
        return self.count