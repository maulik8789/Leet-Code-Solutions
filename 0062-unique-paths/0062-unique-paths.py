class Solution:
    def uniquePaths(self, m: int, n: int, i=0, j=0) -> int:
        # Dynamic Programming - Tabulation
        dp = [[1]*n for i in range(m)]
        print(dp)
        for i, j in product(range(1, m), range(1, n)):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

        # time limit exceeded
        # if m<=i or n<=j:
        #     return 0
        # if i==m-1 and j==n-1:
        #     return 1
        # return self.uniquePaths(m, n, i+1, j) + self.uniquePaths(m, n, i, j+1)