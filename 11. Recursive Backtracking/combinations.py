class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol, result = [], []
        def backtrack(x):
            if len(sol) == k:
                result.append(sol[:])
                return
            left = x
            to_add = k - len(sol)
            # not take
            if left > to_add:
                backtrack(x - 1)
            # take
            sol.append(x)
            backtrack(x - 1)
            sol.pop()

        backtrack(n)
        return result

  # Time Complexity: Beats 91%
