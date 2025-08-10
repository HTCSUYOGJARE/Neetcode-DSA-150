class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1)>len(s2):
            return False
        s1cnt=[0]*26
        s2cnt=[0]*26
        for i in range(len(s1)):
            s1cnt[ord(s1[i])-ord('a')]+=1
            s2cnt[ord(s2[i])-ord('a')]+=1
        matches=0
        for i in range(26):
            matches+=(1 if s1cnt[i]==s2cnt[i] else 0)
        l=0
        for r in range(len(s1),len(s2)):
            if matches==26:
                return True

            index=ord(s2[r])-ord("a")
            s2cnt[index]+=1
            if s1cnt[index]==s2cnt[index]:
                matches+=1
            elif s1cnt[index]+1==s2cnt[index]:
                matches-=1

            index=ord(s2[l])-ord("a")
            s2cnt[index]-=1
            if s1cnt[index]==s2cnt[index]:
                matches+=1
            elif s1cnt[index]-1==s2cnt[index]:
                matches-=1
            l+=1
        return matches==26