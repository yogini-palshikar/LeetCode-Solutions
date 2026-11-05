class MinStack:

    def __init__(self):
        self.l=[]
        self.minl=[]

    def push(self, val: int) -> None:
        self.l.append(val)
        if len(self.minl)==0 or val <= self.minl[-1]:
            self.minl.append(val)

    def pop(self) -> None:
        if(len(self.l)==0):
            return -1
        
        n = self.l.pop(-1)
        if n==self.minl[-1]:
            self.minl.pop()

    def top(self) -> int:
        if(len(self.l)==0):
            return -1
        return self.l[-1]

    def getMin(self) -> int:
        return self.minl[-1]
            
