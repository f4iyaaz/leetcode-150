class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        original_size = len(nums)
        mutated = set(nums)
        mutated_size = len(mutated)
        if mutated_size == original_size:
            return False
        
        return True

  # Runtime: Beats 94%
  # Memory: Beats 85%
