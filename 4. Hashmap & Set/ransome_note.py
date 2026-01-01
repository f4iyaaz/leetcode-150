class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = {}
        for c in magazine:
            if c in mag:
                mag[c] += 1
            else:
                mag[c] = 1
        for c in ransomNote:
            if c not in mag:
                return False
            elif mag[c] == 1:
                del mag[c]
            else:
                mag[c] -= 1
        return True

  # Runtime: Beats 26%
  # Memory: Beats 70%
