class MinStack:

    def __init__(self):
        self.myStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.myStack.append(val)
        if not(self.minStack):
            self.minStack.append(val)
        else:
            val = min(self.minStack[-1],val)
            self.minStack.append(val)

    def pop(self) -> None:
        self.myStack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.myStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
