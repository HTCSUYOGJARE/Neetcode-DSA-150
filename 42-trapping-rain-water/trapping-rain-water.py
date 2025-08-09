class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        prefix=0
        suffix=0
        pre=[0]*len(height)
        for i in range(len(height)):
            pre[i]=prefix
            prefix = max(prefix,height[i])
        suf=[0]*len(height)
        for j in range(len(height)-1,-1,-1):
            suf[j]=suffix
            suffix = max(suffix,height[j])
        res=0
        for i in range(len(height)):
            if (min(pre[i],suf[i])-height[i])>=0:
                res+=(min(pre[i],suf[i])-height[i])
        return res
