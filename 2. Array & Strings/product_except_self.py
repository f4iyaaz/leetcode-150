class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums) 
        for i in range(1, len(nums)):
            left[i] = nums[i - 1] * left[i - 1]
        for k in range(len(nums) - 2, -1, -1):
            right[k] = nums[k + 1] * right[k + 1]
        
        product = [x * y for x, y in zip(left, right)]
        return product

  # Runtime: Beats 26%
