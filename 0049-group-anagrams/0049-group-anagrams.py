class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cpy=strs[:]
       
        
        #sort string
        for i in range(0,len(cpy)):
            cpy[i]="".join(sorted(cpy[i]))
        
        
        #dict of sorted string and original value
        d1=dict(zip(strs,cpy))
        
        d={}
        #group according to same key
        for i in strs:
            key=d1[i]
            d.setdefault(key,[]).append(i)
        
        cpy.clear()
        for i in d:
            cpy.append(d[i])

        return cpy
        
           


