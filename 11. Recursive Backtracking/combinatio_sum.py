class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        nums = candidates
        n = len(nums)

        def backtrack(i, sum):
            if sum == target:
                res.append(sol[:])
                return

            if sum > target or i == n:
                return
            # not take
            backtrack(i + 1, sum)
            # take
            sol.append(nums[i])
            backtrack(i, sum + nums[i])
            sol.pop()
    
        backtrack(0, 0)
        return res
