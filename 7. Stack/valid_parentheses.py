class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        closing_bracket = {')': '(', '}': '{', ']': '['}
        stack = []
        for p in s:
            if p not in closing_bracket:
                stack.append(p)
            else:
                if len(stack) > 0 and closing_bracket[p] == stack[len(stack) - 1]:
                    stack.pop()
                else:
                    return False
        if len(stack) > 0:
            return False
        else:
            return True
