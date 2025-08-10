class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        S =set()
        i=0
        j=i+1
        res=1
        while i<j & j<len(s):
            if s[i]!=s[j]:
                S.add(s[i])
                if (s[j] not in S):
                    S.add(s[j])
                    res=max(res,len(S))
                    j+=1
                else:
                    res=max(res,len(S))
                    S.clear()
                    i+=1
                    j=i+1
            else:
                res=max(res,len(S))
                S.clear()
                i+=1
                j=i+1

        return res