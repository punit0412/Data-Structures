class Stack:

    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    def size_of_stack(self):
        return len(self.stack)

    def is_empty(self):
        return self.stack == []


stack = Stack()
stack.push(2)
stack.push(5)
stack.push(6)
print(f"Size of stack : {stack.size_of_stack()}")
print(f"popped item is : {stack.pop()}")
