class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        Max = 0
        for i in nums:
            if i == 1:
                count += 1
                Max = max(count, Max)
            else:
                count = 0
        return  Max
        