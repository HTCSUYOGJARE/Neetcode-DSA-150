class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def anagram(s):
            S={}
            for i in s:
                if i in S:
                    S[i]+=1
                else:
                    S[i]=1
            return S
        res={}
        for i in strs:
            S=[0]*26
            for j in i:
                S[ord(j)-ord('a')]+=1
            if tuple(S) in res:
                res[tuple(S)].append(i)
            else:
                res[tuple(S)]=[i]
        Res=[]
        for k,v in res.items():
            Res.append(v)
        return Res
                