class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:  # empty subRoot is always a subtree
            return True
        if not root:     # main tree is empty but subRoot not
            return False

        def isSame(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and isSame(p.left, q.left) and isSame(p.right, q.right)

        # BFS / DFS traversal of root
        def dfs(node):
            if not node and subRoot:
                return False
            if node.val == subRoot.val and isSame(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
