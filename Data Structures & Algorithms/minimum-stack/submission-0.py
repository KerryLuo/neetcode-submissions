from collections import deque

class MinStack:

    def __init__(self):
        self.stack = deque()
        self.currentMin = deque()

    def push(self, val: int) -> None:
        if not self.currentMin:
            self.currentMin.append(val)
        else:
            self.currentMin.append(min(val, self.currentMin[-1]))
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.currentMin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.currentMin[-1]
