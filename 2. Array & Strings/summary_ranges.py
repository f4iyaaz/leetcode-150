class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        r = ""
        for i in range(len(nums)):
            if i == len(nums) - 1:
                if nums[i] - nums[i - 1] == 1:
                    ranges.append(r)
                    break
                else:
                    ranges.append(str(nums[i]))
                    break
            diff = abs(nums[i] - nums[i + 1])
            if diff == 1:
                if r == "":
                    first = str(nums[i])
                    second = str(nums[i + 1])
                    r = first + "->" + second
                else:
                    num = str(nums[i + 1])
                    r = first + "->" + num
            else:
                if r != "":
                    ranges.append(r)
                    r = ""
                else:
                    ranges.append(str(nums[i]))
        return ranges

# Runtime: Beats 100%


