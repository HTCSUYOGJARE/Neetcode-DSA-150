class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res=[]
        d=deque() # index deque
        l,r=0,0

        while r<len(nums):
            while d and nums[r]>nums[d[-1]]:
                d.pop()
            d.append(r)

            if d[0]<l:
                d.popleft()
            
            if (r+1)>=k:
                res.append(nums[d[0]])
                l+=1
            r+=1
        return res