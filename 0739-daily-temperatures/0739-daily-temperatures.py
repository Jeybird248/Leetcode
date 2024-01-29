class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                curr = stack.pop()
                output[curr] = idx - curr
            stack.append(idx)
        return output