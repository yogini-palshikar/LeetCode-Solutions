class Solution:
    def __init__(self):
        self.l=[]
    
    def push(self,s):
        self.l.append(s)
    def top(self):
        if(len(self.l)==0):
            return -1
        return self.l[-1]

    def check(self,o,c):
        if(o=='(' and c==')'):
            return True
        elif(o=='[' and c==']'):
            return True
        elif(o=='{' and c=='}'):
            return True
        else:
            return False

    def isValid(self, s: str) -> bool:
        for i in range(0,len(s)):
            if (s[i]=='(' or s[i]=='{' or s[i]=='['):
                self.push(s[i])
            elif (s[i]==')' or s[i]=='}' or s[i]==']'):
                t=self.top()
                if (self.check(t,s[i])):
                    self.l.pop()
                else:
                    return False
        if len(self.l)==0:
            return True
        else:
            return False
