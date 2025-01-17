# Time:  O(m * n)
# Space: O(n)

import collections


# dp, optimized from solution2
class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        if (len(grid)+len(grid[0])-1)%2:
            return False
        dp = [[float("inf"), float("-inf")] for _ in xrange(len(grid[0])+1)]
        for i in xrange(len(grid)):
            dp[0] = [0, 0] if not i else [float("inf"), float("-inf")]
            for j in xrange(len(grid[0])):
                d = 1 if grid[i][j] == '(' else -1
                dp[j+1] = [min(dp[j+1][0], dp[j][0])+d, max(dp[j+1][1], dp[j][1])+d]
                if dp[j+1][1] < 0:
                    dp[j+1] = [float("inf"), float("-inf")]
                else:
                    dp[j+1][0] = max(dp[j+1][0], dp[j+1][1]%2)
        return dp[len(grid[0])][0] == 0


# Time:  O((m * n) * (m + n) / 32)
# Space: O(n * (m + n) / 32)
# dp
class Solution2(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        if (len(grid)+len(grid[0])-1)%2:
            return False
        dp = [0]*(len(grid[0])+1)
        for i in xrange(len(grid)):
            dp[0] = int(not i)
            for j in xrange(len(grid[0])):
                dp[j+1] = (dp[j]|dp[j+1])<<1 if grid[i][j] == '(' else (dp[j]|dp[j+1])>>1
        return dp[-1]&1
