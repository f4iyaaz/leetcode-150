class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low = 1
        high = num
        mid = (low + high) // 2
        while low <= high:
            if (mid * mid) == num:
                return True
            elif (mid * mid) > num:
                high = mid - 1
                mid = (low + high) // 2
            else:
                low = mid + 1
                mid = (low + high) // 2

        return False

  # Runtime: Beats 100%
  # Memory: Beats 99.24%
