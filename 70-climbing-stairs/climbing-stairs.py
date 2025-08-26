class Solution:
    def climbStairs(self, n: int) -> int:
        def countways(n,memo):
            if n<0:
                return 0
            if n==0:
                return 1

            if memo[n]!=-1:
                return memo[n]
            
            memo[n]=countways(n-1,memo)+countways(n-2,memo)

            return memo[n]

        def memo_creation(n):
            memo = [-1]*(n+1)
            return countways(n,memo)
        
        return memo_creation(n)
        