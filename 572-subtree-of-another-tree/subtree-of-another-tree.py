# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(root,subroot):
            if not root:
                return deque()
            stack =deque([root])
            match_stack=deque()
            while stack:
                node = stack.popleft()
                if node.val == subroot.val:
                    match_stack.append(node)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            return match_stack
        def match(p,q):
            if not p and not q: return True
            if not p or not q: return False
            return p.val==q.val and match(p.left,q.left) and match(p.right,q.right)
        candidates = check(root,subRoot)
        return any (match(node,subRoot) for node in candidates)