class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, zeros, max_w = 0, 0, 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            window = r - l + 1
            max_w = max(max_w, window)
        return max_w

  # Runtime: Beats 83%
