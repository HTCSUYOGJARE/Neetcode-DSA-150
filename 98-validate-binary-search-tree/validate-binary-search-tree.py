# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(node):
            if not node:
                return []
            return dfs(node.left)+[node.val]+dfs(node.right)
        s=dfs(root)
        i,j=0,1
        while i<j and j<len(s):
            if s[i]>=s[j]:
                return False
                break
            i+=1
            j+=1
        return True