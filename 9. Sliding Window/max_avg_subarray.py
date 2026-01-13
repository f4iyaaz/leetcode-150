class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = 0
        total = 0
        for i in range(k):
            total += nums[i]
        max_avg = total / k

        for i in range(k, len(nums)):
            total += nums[i]
            total -= nums[i - k]
            max_avg = max(max_avg, (total / k))
        
        return max_avg

  # Runtime: Beats 80%
