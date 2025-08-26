class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        nums=[0]*(len(cost)+1)
        nums[0]=0
        nums[1]=0

        for i in range(2,len(cost)+1):
            nums[i] = min(nums[i-1]+cost[i-1],nums[i-2]+cost[i-2])
        return nums[len(cost)]