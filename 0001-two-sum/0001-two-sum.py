class Solution(object):
    def twoSum(self, nums, target):
        l=len(nums)
        l1=[]
        for i in range(0,l-1):
            for j in range(i+1,l):
                if (nums[i]+nums[j]==target) :
                    l1.append(i)
                    l1.append(j)
                    return l1

        