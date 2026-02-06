class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        res, sol = [], []
        def backtrack(i):
            if i == length:
                res.append(sol[:])
                return
            #  don't pick
            backtrack(i + 1)
            # pick
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()
        
        backtrack(0)
        return res
      
  # Time Complexity: O(2^n)
  # Runtime: Beats 100%
