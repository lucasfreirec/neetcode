class MinStack:

    def __init__(self):
        self.stack = []
        self.aux = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if not self.aux:
            self.aux.append(val)
        else:
            self.aux.append(min(val, self.aux[-1]))


    def pop(self) -> None:
        self.stack.pop()
        self.aux.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.aux[-1]
