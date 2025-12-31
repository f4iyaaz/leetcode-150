class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        total_length = len(word1) + len(word2)
        w1 = deque(word1)
        w2 = deque(word2)
        merged_string = ""
        for i in range(total_length):
            if i % 2 == 0 and w1 or not w2:
                merged_string += w1[0]
                w1.popleft()
            elif w2 or not w1:
                merged_string += w2[0]
                w2.popleft()

        return merged_string

  # Runtime: Beats 75%
  # Memory: Beats 86%
