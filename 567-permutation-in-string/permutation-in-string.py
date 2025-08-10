class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        S1=defaultdict(int)
        for i in s1:
            S1[i]+=1
        i=0
        while i<(len(s2)-len(s1)+1):
            if s2[i] not in S1:
                i+=1
            else:
                d=defaultdict(int)
                for k in range(i,i+len(s1)):
                    d[s2[k]]+=1
                if d==S1:
                    return True
                i+=1
        return False