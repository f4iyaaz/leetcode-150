class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2}
        def fib(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = fib(n - 2) + fib(n - 1)
                return memo[n]
        return fib(n)

  # Runtime: Beats 100%
