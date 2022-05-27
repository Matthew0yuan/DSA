import numpy as np
class DSAstack():
    max = 100
    def __init__(self):
        self.count = 0
        self.stack = np.empty(self.max, dtype=object)

    def getcount(self):
            print("\n count=", self.count)
    
        
    def isEmpty(self):
        if self.count == 0:
            a = True
        else:
            a = False
        return a
    
    def isfull(self):
        a = len(self.stack)
        return a
        
    def display(self):
        print("",self.stack)
        return self.stack
        
    
    def push(self,val):
        if self.isfull() == self.count:
            raise Exception(" stack is Full(Push)")
        else:
            print("\nstack =",self.stack)
            self.stack[self.count] = val
            self.count = self.count + 1
            print("\nstack now= ", self.stack)  
        
    def top(self):
        if self.isEmpty() == True:
            raise Exception("Can't top, stack is empty(top)")
        else:
            self.stack[self.count] = None
            self.topval = self.stack[self.count -1]
            print(" Removed from the top= ", self.topval)
    
    
    def pop(self):
        if self.isEmpty() == True:
            raise Exception("Stack is Empty")
        else:
            self.topval = self.stack[self.count]
            print("\npop= ", self.stack)
                   
        
    
        
    
            
    