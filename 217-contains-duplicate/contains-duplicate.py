class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        res={}
        for i in range(len(nums)):
            if nums[i] in res:
                res[nums[i]]+=1
            else:
                res[nums[i]]=1
        for j in res:
            if res[j]>1:
                return True
        return False
