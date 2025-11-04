class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = "".join(char for char in s if char.isalnum())
        res = res.lower()
        i=0
        j=len(res)-1
        while i<j:
            if res[j]==res[i]:
                i+=1
                j-=1
            else:
                return False
                
        return True