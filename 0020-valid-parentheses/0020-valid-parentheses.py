class Solution:


    def isValid(self, s: str) -> bool:
        m={')':'(', '}':'{', ']':'['}
        l=[]
        for i in s:
            if i in m:
                if(len(l)==0):
                    t = -1
                else:
                    t = l[-1]

                if(m[i]==t):
                    l.pop()
                else:
                    return False
            else:
                l.append(i)
        
        if len(l)==0:
            return True
        else:
            return False
