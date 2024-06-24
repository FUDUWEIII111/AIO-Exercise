class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_empty(self):
        return len(self.__stack) == 0

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def push(self, item):
        if self.is_full():
            raise ValueError('Overflow')
        else:
            self.__stack.append(item)

    def pop(self):
        if self.is_empty():
            raise ValueError('Underflow')
        else:
            self.__stack.pop()

    def top(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        else:
            return self.__stack[-1]


def main():
    stack = MyStack(5)
    stack.push(1)
    stack.top()
    stack.is_empty()
    stack.is_full()
    stack.pop()


if __name__ == "__main__":
    main()
