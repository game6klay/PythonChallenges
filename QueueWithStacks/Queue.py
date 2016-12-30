class Queue:

    def __init__(self,inStack,outStack):
        self.inStack = []
        self.outStack = []

    def enqueue(self, element):
        self.instack.append(element)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()

q = Queue()
for i in range(10):
    q.enqueue(i)
for i in xrange(10):
    print
    q.dequeue(),


