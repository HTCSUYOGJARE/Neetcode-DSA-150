class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d ={}
        buckets = [[] for i in range(len(nums)+1)]
        for i in nums:
            d[i]=1+d.get(i,0)
        for num,freq in d.items():
            buckets[freq].append(num)
        
        res=[]
        for i in range(len(buckets)-1,0,-1):
            for j in buckets[i]:
                res.append(j)
                if len(res)==k:
                    return res

