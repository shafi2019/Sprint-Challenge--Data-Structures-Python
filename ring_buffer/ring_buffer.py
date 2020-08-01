class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.head = 0

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)
        else:
            if self.head == self.capacity:
                self.head = 0
            self.data[self.head] = item
        self.head += 1
            # self.data[self.head] = item
            # self.head = (self.head + 1) self.capacity

    def get(self):
        return self.data