class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        length = 0
        l = 0
        for i in n:
            if (i - 1) not in n:
                length += 1
                val = i
                while val in n:
                    if val + 1 in n:
                        length += 1
                        val += 1
                    else:
                        break
                l = max(length, l)
            length = 0
        return l

  
