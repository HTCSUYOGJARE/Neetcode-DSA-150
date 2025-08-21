class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=set()
        nums.sort()
        def DFS(i,subset):
            if i>=len(nums):
                res.add(tuple(subset.copy()))
                return
            subset.append(nums[i])
            DFS(i+1,subset)
            subset.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            DFS(i+1,subset)
        DFS(0,[])
        return [list(x) for x in res]