class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        length = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                length += 1
        return length