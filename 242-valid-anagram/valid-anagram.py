class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        S ={}
        for i in s:
            if i not in S:
                S[i]=1
            else:
                S[i]+=1
        R={}
        for i in t:
            if i not in R:
                R[i]=1
            else:
                R[i]+=1
        if S==R:
            return True
        else:
            return False
        