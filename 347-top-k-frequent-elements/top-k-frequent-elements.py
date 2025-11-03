class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for i in nums:
            d[i]+=1
        sorted_d = sorted(d.items(),key=lambda x:x[1],reverse=True)
        res=[]
        for i in range(k):
            res.append(sorted_d[i][0])
        return res