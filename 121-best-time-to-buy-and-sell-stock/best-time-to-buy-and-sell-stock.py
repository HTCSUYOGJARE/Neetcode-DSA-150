class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i=0
        j=i+1
        res=0
        while i<j & j<len(prices):
            if prices[j]<prices[i]:
                i=j
                j+=1
            else:
                res=max((prices[j]-prices[i]),res)
                j+=1
        return res