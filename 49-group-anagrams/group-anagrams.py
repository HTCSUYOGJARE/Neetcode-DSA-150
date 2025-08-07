class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        S = defaultdict(list)
        for i in strs:
            count = [0]*26
            for j in i:
                count[ord(j)-ord('a')]+=1
            S[tuple(count)].append(i)
        return list(S.values())

        