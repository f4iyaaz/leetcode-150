class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        length = 0
        tracker = set()
        l, r = 0, 0
        while r < len(s):
            if s[r] not in tracker:
                tracker.add(s[r])
                r += 1
            else:
                length = max((r - l), length)
                if s[l] != s[r]:
                    l += 1
                else:
                    l += 1
                    tracker.clear()
                    for i in range(l, r):
                        tracker.add(s[i])
        length = max((r - l), length)
        return length
