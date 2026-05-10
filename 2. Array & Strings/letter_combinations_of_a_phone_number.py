class Solution:
    def letterCombinations(self, digits: str) -> str:
        mappings = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        output = []
        latest = []
        result = list(mappings[digits[0]])
        for i in range(1, len(digits)):
            temp_list = list(mappings[digits[i]])
            for c in result:
                for k in temp_list:
                    latest.append(c + k)
            result = latest
            latest = []

        output = result
        return output

# Time: beats 100%

