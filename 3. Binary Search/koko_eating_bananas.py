class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return math.ceil(piles[0] / h)
        hours = 0
        minimum_k = 0
        low = 1
        high = max(piles)
        mid = (low + high) // 2
        while low <= high:
            hours = 0
            for i in piles:
                hours += math.ceil(i / mid)
            
            if hours == h:
                minimum_k = mid
                high = mid - 1
                mid = (low + high) // 2
            elif hours > h:
                low = mid + 1
                mid = (low + high) // 2
            else:
                high = mid - 1
                mid = (low + high) // 2
        if minimum_k == 0:
            return low
        else:
            return minimum_k

      # Runtime: Beats 58%
