import numpy as np
class DSAqueue():
    max = 5
    def __init__(self):
        self.count = 0
        self.queue = np.empty(self.max, dtype=object)
    
    def getcount(self):
        print("\n count=", self.count)
    
    def isEmpty(self):
        if self.count == 0:
            a = True
        else:
            a = False
        return a
    
    def isfull(self):
        a = len(self.queue)
        return a
        
    def display(self):
        print(self.queue)
        
    def enqueue(self,Val):
        if self.isfull() == self.count:
            raise Exception("queue is full")
        else:
            self.count = self.count + 1
            for i in range((len(self.queue)-2),-1,-1):
                self.queue[i+1] = self.queue[i]
            self.queue[0] = Val
            print("\nqueue = ", self.queue)