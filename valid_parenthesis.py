class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openchars = "({["
        c = { ")" : "(", "]" : "[", "}": "{"}
        for char in s:
            if char in openchars:
                stack.append(char)
            elif len(stack) > 0 and stack[-1] == c.get(char):
                stack.pop()
            else:
                return False
        if len(stack) > 0: 
            return False
        return True
