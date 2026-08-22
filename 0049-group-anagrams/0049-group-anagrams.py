class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cpy=strs[:]
        for i in range(0,len(cpy)):
            cpy[i]="".join(sorted(cpy[i]))
        s=set(cpy)
        result=[]
        for i in s:
            l=[]
            for j in range(0,len(cpy)):
                if(i==cpy[j]):
                    l.append(strs[j])
            result.append(l)
        return result
        
           


