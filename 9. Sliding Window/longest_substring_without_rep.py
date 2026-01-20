class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        counter = {}
        left, right = 0, 0
        size = 0
        length = len(s)
        for c in s:
            counter[c] = 0
        while right < length:
            if counter[s[right]] < 2:
                counter[s[right]] += 1
                if counter[s[right]] > 1:
                    continue
                else:
                    right += 1
            else:
                if s[left] == s[right]:
                    size = max(size, (right - left))
                    counter[s[left]] -= 1
                    left += 1
                    right += 1
                else:
                    size = max(size, (right - left))
                    counter[s[left]] -= 1
                    left += 1
        size = max(size, (right - left))
        return size
