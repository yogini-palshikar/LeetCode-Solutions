class Solution:
    def __init__(self):
        self.l=[]
    
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
                self.l.append(s[i])

            elif (s[i]==')' or s[i]=='}' or s[i]==']'):
                
                if(len(self.l)==0):
                    t = -1
                else:
                    t = self.l[-1]
                
                if (self.check(t,s[i])):
                    self.l.pop()
                else:
                    return False
        
        if len(self.l)==0:
            return True
        else:
            return False
