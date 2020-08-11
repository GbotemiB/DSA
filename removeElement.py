class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x=nums.count(val)
        y = len(nums)
        a=[]
        temp=0
        for i in range(x):
            nums.remove(val)
        