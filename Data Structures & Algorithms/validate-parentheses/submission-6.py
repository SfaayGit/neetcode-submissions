class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "]": "[", "}": "{"}
        for word in s:
            if (word == '{' or word == '(' or word == '['):
                stack.append(word)
            else:
                if (not stack):
                    return False
                top = stack.pop()
                if (pairs[word] != top):
                    return False
        return len(stack) == 0