class QueueError(IndexError):  # Choose base class for the new exception.
    def __init__(self):
        IndexError.__init__(self)


class Queue:
    def __init__(self):
        self.list = []

    def put(self, elem):
        self.list = str(elem).split() + self.list

    def get(self):
        if len(self.list) <=0:
            raise QueueError
        val = self.list[-1]
        del self.list[-1]
        return val
    def printQueue(self):
        for item in self.list:
            print(item)

class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)

    def isEmpty(self):
        if len(self.list) <= 0:
            return True
        return False

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isEmpty():
        print(que.get())
    else:
        print("Queue empty")
