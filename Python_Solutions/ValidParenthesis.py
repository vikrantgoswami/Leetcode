class Solution:
    def isValid(self, s: str) -> bool:
        map = {')':'(', '}':'{', ']':'['}
        stack = []
        for character in s:
            if character in map.values():
                stack.append(character)
            else:
                if len(stack) >= 1 and stack[-1] == map[character]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0