class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = {
            "(":")",
            "{": "}",
            "[": "]"
        }

        for i in s:
            if i in opening:
                stack.append(i)
            else:
                if(len(stack) == 0 ):
                    return False
                elif(opening.get(stack[-1]) != i):
                    return False
                else:
                    stack.pop()

        return len(stack) == 0