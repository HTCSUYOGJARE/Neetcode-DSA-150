class Solution(object):
    def isPalindrome(self, s):
        cleaned_s = ''.join([char for char in s if char.isalnum()])
        S = cleaned_s.lower()
        n = len(S)
        Output = all(S[i] == S[-(i+1)] for i in range(n//2))
        return Output
        