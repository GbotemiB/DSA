class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        m=[]
        for i in range(len(nums)):
            if nums[i] == 1:
                m.append(i)
        for i in range(len(m)-1):
            if (k < (m[i+1] - m[i])) == False:
                return False
        return True