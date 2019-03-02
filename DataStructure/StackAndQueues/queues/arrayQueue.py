class Queue:
    def __init__(self, capacity):
        self.data = [0]*capacity
        self.front = 0
        self.back = 0
        self.capacity = capacity

    def enqueue(self, val):
        if self.back < self.capacity:
            self.data[self.back] = val
            self.back += 1
            return True
        else:
            print("Queue is full")
            return False

    def dequeue(self):
        if self.back == self.front:
            print("Queue is empty")
            return False
        else:
            self.data[self.front] = 0
            self.front += 1
            return True

    def display(self):
        for i in range(self.front, self.back):
            print(self.data[i], end=' ')

        print()

    def peek(self):
        if self.front != self.back:
            return self.data[self.front]
        else:
            pass
    def isEmpty(self):
      if self.front==self.back:
        return True
      else:
        return False
