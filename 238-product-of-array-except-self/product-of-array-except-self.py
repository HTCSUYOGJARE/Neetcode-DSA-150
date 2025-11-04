class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for i in range(len(nums)-1):
            prefix.append(prefix[-1]*nums[i])
        suffix=[1]
        for j in range(len(nums)-1,0,-1):
            suffix.append(suffix[-1]*nums[j])
        suffix = suffix[::-1]
        res=[]
        for u,v in zip(prefix,suffix):
            res.append(u*v)
        return res