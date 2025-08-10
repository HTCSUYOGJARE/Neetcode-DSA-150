class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res=0
        count={}
        l=0
        for r in range(len(s)):
            count[s[r]]=1+count.get(s[r],0) # noting the count of each character
            

            while (r-l+1-max(count.values()))>k: # checking the possible replacements, if windowlen-max frequnecy bigger than k then need to move l
                count[s[l]]-=1
                l+=1
            res= max(res,r-l+1)
        return res
        