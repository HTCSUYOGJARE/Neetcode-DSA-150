class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix=[]
        i=0
        while i<len(nums):
            if i==0:
                prefix.append(1)
            else:
                prefix.append(nums[i-1]*prefix[-1])
            i+=1

        suffix=[]
        j=len(nums)-1
        while j>=0:
            if j==(len(nums)-1):
                suffix.append(1)
            else:
                suffix.append(nums[j+1]*suffix[-1])
            j-=1

        suf=[]
        for i in range(len(suffix)-1,-1,-1):
            suf.append(suffix[i])

        res=[]
        for i,j in zip(prefix,suf):
            res.append(i*j)
        return res
