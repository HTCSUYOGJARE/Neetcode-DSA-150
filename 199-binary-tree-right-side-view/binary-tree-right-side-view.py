# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def level_list(root):
            if not root:
                return []
            
            res = []
            q = deque([root])
            
            while q:
                level_nodes = []
                for _ in range(len(q)):   # process all nodes in current level
                    node = q.popleft()
                    level_nodes.append(node.val)
                    
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                res.append(level_nodes)   # one list per level
            
            return res
        level_list = level_list(root)
        res=[]
        for i in level_list:
            res.append(i[-1])
        return res