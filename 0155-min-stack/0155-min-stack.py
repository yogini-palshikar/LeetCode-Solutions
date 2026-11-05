class MinStack:

    def __init__(self):
        self.l=[]
        self.minl=[]

    def push(self, value: int) -> None:
        self.l.append(value)

        if(len(self.minl)==0 or self.minl[-1]>=value):
            self.minl.append(value)

    def pop(self) -> None:
        if (len(self.l)!=0):
            if self.l[-1] == self.minl[-1]:
                self.minl.pop()
            self.l.pop()
        else:
            return None

    def top(self) -> int:
        if(len(self.l)!=0):
            return self.l[-1]
        else:
            return None

    def getMin(self) -> int:
        if len(self.minl)!=0:
            return self.minl[-1]
        else:
            return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()