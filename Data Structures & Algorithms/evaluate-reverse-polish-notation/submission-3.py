class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def calculate(p1,p2, op):
            match op:
                case "+":
                    return p1 + p2
                case "-":
                    return p1 - p2
                case "/":
                    return int(p1/p2)
                case "*":
                    return p1 * p2
                case _:
                    return ValueError("Not a valid operator")

        for i in tokens:
            if i not in ["+", "-", "/", "*"]:
                stack.append(i)
            else:
                
                p2 = int(stack.pop())
                p1 = int(stack.pop())

                stack.append(calculate(p1, p2, i))
        
        return int(stack.pop())





        