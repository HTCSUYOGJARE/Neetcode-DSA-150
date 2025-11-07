class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_val = piles[0]
        for i in piles:
            if i>max_val:
                max_val=i
        l=1
        r=max_val
        res=0
        while l<=r:
            mid = (l+r)//2
            time = 0
            for i in piles:
                time+=math.ceil(i/mid)
            if time>h:
                l=mid+1
            elif time<=h:
                r=mid-1
                res=mid
        return res
