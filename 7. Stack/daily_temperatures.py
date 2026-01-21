class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        days = [0] * length
        t = temperatures
        stk = []
        for i, temp in enumerate(t):
            while stk and temp > stk[-1][0]:
                days[stk[-1][1]] = i - stk[-1][1]
                stk.pop()
            stk.append((temp, i))
        return days
