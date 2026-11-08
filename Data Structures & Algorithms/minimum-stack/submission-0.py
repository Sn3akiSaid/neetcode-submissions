class MinStack:

    def __init__(self):
        # stacks in python can be implemented as lists
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # Add val into regular stack
        self.stack.append(val)
        
        # Redefine val to be either a new minimum or the previous minimum 
        # from top of minStack
        # if minStack is empty just compare with the val itself
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # Get top of minStack (the smallest num b)
        return self.minStack[-1]
