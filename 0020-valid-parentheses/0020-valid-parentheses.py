class Solution:


    def isValid(self, s: str) -> bool:
        m={')':'(', '}':'{', ']':'['}
        l=[]
        for i in s:
            if i in m:
                if  not l or l.pop()!=m[i]:
                    return False 
            else:
                l.append(i)
        
        if len(l)==0:
            return True
        else:
            return False
