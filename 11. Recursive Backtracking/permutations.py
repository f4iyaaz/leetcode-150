class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        length = len(nums)

        def backtrack():
            if len(sol) == length:
                res.append(sol[:])
                return
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
            
        backtrack()
        return res

  # Time Complexity: O(n!)
