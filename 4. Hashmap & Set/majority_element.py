class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_count = 0
        element = 0
        for i in count:
            if count[i] > max_count:
                max_count = count[i]
                element = i
        return element

  # Runtime: Beats 85%
