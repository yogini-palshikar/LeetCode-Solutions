class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=dict(Counter(nums))
        d1=dict(sorted(d.items(), key=lambda item:item[1], reverse=True))
        l=[]
        for i in range(0,k):
            l.append(list(d1.keys())[i])
        return l
        