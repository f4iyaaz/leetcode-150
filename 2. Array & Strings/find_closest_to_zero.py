class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        min = float("inf")
        flag = False
        nums.sort()
        for i in range(len(nums)):
            if i != 0:
                d = abs(nums[i]) - 0
                if d == distance:
                    flag = True
                    continue
                elif d > distance:
                    return nums[i-1]
            distance = abs(nums[i]) - 0
        if flag:
            return nums[i]

      # Runtime: Beats 64.73%
      # Memory: Beats 63.5%
