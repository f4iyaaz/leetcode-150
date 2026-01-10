class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in track:
                return [i, track[diff]]
            else:
                track[nums[i]] = i


# Runtime: Beats 100%
