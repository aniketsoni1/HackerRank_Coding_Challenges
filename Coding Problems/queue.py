"""
FIFO
Queue = []
Queue = [1,2,3,4] push
[2,3,4] pop
[3,4] pop
[4] pop
[] pop
empty stack

"""


class Queue(object):
    def __init__(self):
        self.queue = []
        self.length = 0

    def enque(self, data):
        self.queue.append(data)
        self.length += 1

    def deque(self):
        if self.length < 1:
            return None
        data = self.queue[0]
        self.queue = self.queue[1:self.length + 1]
        self.length -= 1
        return data


def main():
    new_queue = Queue()
    new_queue.enque(1)
    new_queue.enque(2)
    new_queue.enque(3)
    new_queue.enque(4)
    print(new_queue.deque())  # 1
    print(new_queue.deque())  # 2
    print(new_queue.deque())  # 3
    print(new_queue.deque())  # 4
    print(new_queue.deque())  # None
    print(new_queue.deque())  # None


if __name__ == '__main__':
    main()