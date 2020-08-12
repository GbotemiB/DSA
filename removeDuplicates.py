class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=[]
        for i in range(len(nums)):
            if len(set(nums)) == 1:
                return 1
            if nums[i-1]==nums[i]:
                pass
            else:
                a.append(nums[i])

        for n, i in enumerate(a):
           nums[n] = a[n]

        return len(a)