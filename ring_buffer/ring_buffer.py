class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.head = 0

    def append(self, item):
        if len(self.data) < self.capacity:
            # Append an element overwriting the oldest one.
            self.data.append(item)
        else:
            if self.head == self.capacity:
                self.head = 0
            self.data[self.head] = item
        self.head += 1
        # set data 'el' value to item

    def get(self):
        return self.data

         # return elements in order