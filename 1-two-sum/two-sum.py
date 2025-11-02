class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i

        for idx,val in enumerate(nums):
            if target-val in d and idx!=d[target-val]:
                return [idx,d[target-val]]
            continue