class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        counter = 0
        for i in nums:
            if i == 0:
                count = max(count, counter)
                counter = 0
            elif i == 1:
                counter +=1 
        count = max(count, counter)
        return count

  # Runtime: Beats 66%
