class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_count = Counter(text)
        if any(c not in text_count for c in text_count):
            return 0
        else:
            return min(text_count['b'], text_count['a'], text_count['l'] // 2, text_count['o'] // 2, text_count['n'])


# Runtime: Beats 100%
# Memory: Beats 92%
