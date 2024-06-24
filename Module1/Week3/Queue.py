class Queue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def enqueue(self, item):
        if self.is_full():
            raise ValueError('Overflow')
        else:
            self.__queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise ValueError('Underflow')
        else:
            self.__queue.pop(0)

    def front(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        else:
            return self.__queue[0]


def main():
    my_queue = Queue(5)
    my_queue.enqueue(10)
    my_queue.enqueue(20)
    my_queue.enqueue(30)
    my_queue.dequeue()
    print(my_queue.front())
    my_queue.is_empty()
    my_queue.is_full()


if __name__ == "__main__":
    main()
