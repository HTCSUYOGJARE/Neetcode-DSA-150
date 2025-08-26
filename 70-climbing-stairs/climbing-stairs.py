class Solution:
    def climbStairs(self, n: int) -> int:
        nums=[0]*(n+1)
        nums[0]=1
        nums[1]=1

        for i in range(2,n+1):
            if nums[i-1]>0:
                nums[i]+=nums[i-1]
            if nums[i-2]>0:
                nums[i]+=nums[i-2]
        return nums[n]
        