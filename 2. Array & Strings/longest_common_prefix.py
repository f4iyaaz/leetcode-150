class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minimum = len(strs[0])
        prefix = ""
        for i in range(1, len(strs)):
            if len(strs[i]) < minimum:
                minimum = len(strs[i])
        
        inner = 0
        while inner < minimum:
            i = 0
            k = 1
            while k < len(strs):
                if strs[i][inner] == strs[k][inner]:
                    k += 1
                    i += 1
                else:
                    return prefix
            prefix += strs[i][inner]
            inner += 1
        return prefix

  # Runtime: Beats 100%
