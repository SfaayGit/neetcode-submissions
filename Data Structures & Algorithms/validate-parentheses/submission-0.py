class Solution:
    def isValid(self, s: str) -> bool:
        opening = "{(["
        closing = "})]"
        stack = []
        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if not stack or opening.index(stack.pop()) != closing.index(char):
                    return False
        return not stack