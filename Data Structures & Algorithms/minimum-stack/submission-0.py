class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minimum = val

        if(len(self.minStack)):
            minimum = min(self.minStack[-1], val)
            
        self.minStack.append(minimum)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        # update min

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


"""

[1], min=1

[1,2], min=1
[1,2,0], min=0
[1,2], min=1

[1,0]



"""
