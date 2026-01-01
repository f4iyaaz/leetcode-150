# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        mid = (low + high) // 2
        while low <= high:
            if isBadVersion(mid) is False:
                low = mid + 1
                mid = (low + high) // 2
            elif isBadVersion(mid) is True:
                high = mid - 1
                mid = (low + high) // 2
        return low

  # Runtime: Beats 14.14%
  # Memory: Beats 88%
