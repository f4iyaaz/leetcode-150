class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = Counter(t)
        flag = len(s) == len(t)
        if flag:
            for k in s_count:
                if s_count[k] == t_count[k]:
                    continue
                else:
                    flag = False
                    break
            if flag:
                return True
            else:
                return False
        else:
            return False

    # Runtime: Beats 98%
    # Memory: Beats 53% 
