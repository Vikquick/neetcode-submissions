class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(', ']':'[', '}':'{'}
        stack = []
        for char in s:
            if char in '{[(':
                stack.append(char)
            else:
                if not stack or stack[-1] != pairs[char]:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0
                