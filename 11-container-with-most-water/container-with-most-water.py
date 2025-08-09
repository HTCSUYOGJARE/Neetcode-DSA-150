class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        res=0
        while i<j:
            l=min(height[i],height[j])*(j-i)
            res=max(res,l)
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return res