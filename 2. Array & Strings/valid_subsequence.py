class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        s_length = len(s)
        t_length = len(t)
        result = ""
        k = 0
        for i in range(t_length):
            if k < s_length and t[i] == s[k]:
                result += t[i]
                k += 1
        if len(result) == s_length:
            return True
        else:
            return False


# Runtime: Beats 100%
