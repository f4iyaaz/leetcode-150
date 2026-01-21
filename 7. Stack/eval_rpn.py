class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        def op(n1, n2, operator):
            x = int(n1)
            y = int(n2)
            if operator == '+':
                return x + y
            elif operator == '-':
                return x - y
            elif operator == '*':
                return x * y
            else:
                return int(x / y)

        stk = []
        result = 0
        for t in tokens:
            if t == '+' or t == '*' or t == '/' or t == '-':
                result = op(stk[-2], stk[-1], t)
                stk.pop()
                stk.pop()
                stk.append(result)
            else:
                stk.append(t)
        return result

  # Runtime: Beats 64%
