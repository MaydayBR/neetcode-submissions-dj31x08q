class Solution:
    def isValid(self, s: str) -> bool:
        opening = {"(" , "[" , "{"}
        closing = {")":"(" , "]":"[" , "}":"{"}
        stack = []
        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if len(stack) < 1:
                    return False
                character_removed = stack.pop()
                character_needed = closing[char]
                if character_removed != character_needed:
                    return False
        return len(stack) == 0