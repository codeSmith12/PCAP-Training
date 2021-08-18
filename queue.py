class QueueError(IndexError):  # Choose base class for the new exception.
    def __init__(self):
        IndexError.__init__(self)


class Queue:
    def __init__(self):
        self.__list = []

    def put(self, elem):
        self.__list = str(elem).split() + self.__list


    def get(self):
        if len(self.__list) <=0:
            raise QueueError
        val = self.__list[-1]
        del self.__list[-1]
        return val
    def printQueue(self):
        for item in self.__list:
            print(item)


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
