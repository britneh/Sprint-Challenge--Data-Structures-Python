class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    class __Full:
        def append(self, item):
            self.data[self.cur] = item
            self.cur = (self.cur+1) % self.capacity

        def get(self):
            return self.data[self.cur:]+self.data[:self.cur]

    def append(self,item):
        """append an element at the end of the buffer"""
        self.data.insert(item)
        if len(self.data) == self.capacity:
            self.cur = 0
            # Permanently change self's class from non-full to full
            self.__class__ = self.__Full

    def get(self):
        """ Return a list of elements from the oldest to the newest. """
        return self.data