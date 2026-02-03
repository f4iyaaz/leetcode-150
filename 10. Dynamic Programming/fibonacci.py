class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def fibonacci(n):
            if n in memo:
                return memo[n]
            if n == 1:
                return 1
            elif n == 0:
                return 0
            memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return memo[n]
        result = fibonacci(n);
        return result
