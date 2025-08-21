class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def DFS(curr,SET):
            if len(curr)==len(nums):
                res.append(curr.copy())
                return
            for i in SET:
                curr.append(i)
                S = SET.copy()
                S.discard(i)
                DFS(curr,S)
                curr.pop()
        DFS([],set(nums))
        return res
