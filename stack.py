
class Stack:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.__items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.__items[-1]
        else:
            return None

stack = Stack()

print(stack.is_empty())

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.is_empty())

print(stack.peek())

#print(stack.items)