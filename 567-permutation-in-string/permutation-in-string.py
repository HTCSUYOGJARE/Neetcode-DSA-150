class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        r=len(s1)-1
        S1 = defaultdict(int)
        for i in s1:
            S1[i]+=1
        while r<len(s2):
            S2 = defaultdict(int)
            for j in range(l,r+1):
                S2[s2[j]]+=1
            if S2==S1:
                return True
            else:
                r+=1
                l+=1
        return False
                    
            


