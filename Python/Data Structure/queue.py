class Queue:
    def __init__(self, n):
        self.n = n
        self.queue = [None] * (n + 1)
        self.head = 0
        self.tail = 0
    def enqueue(self, x):
        self.queue[self.tail] = x
        if self.tail == self.n:
            self.tail = 0
        else:
            self.tail += 1
    def dequeue(self):
        x = self.queue[self.head]
        if self.head == self.n:
            self.head = 0
        else:
            self.head += 1
        return x
    def is_empty(self):
        if self.head == self.tail:
            return True
        else:
            return False