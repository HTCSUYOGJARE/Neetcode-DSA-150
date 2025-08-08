class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d =defaultdict(int)
        for i in nums:
            d[i]+=1
        freq=[[] for i in range(len(nums)+1)]
        for i,j in d.items():
            freq[j].append(i)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                if len(res)<k:
                    res.append(num)
        return res

                