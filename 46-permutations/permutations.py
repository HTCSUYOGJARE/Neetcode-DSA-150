class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def BFS(curr,SET):
            if len(curr)==len(nums):
                res.append(curr.copy())
                return
            for i in SET:
                curr.append(i)
                S = SET.copy()
                S.discard(i)
                BFS(curr,S)
                curr.pop()
        BFS([],set(nums))
        return [list(x) for x in res]
