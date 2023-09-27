class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if len(f"{n:b}".replace("0","")) == 1:
            return True
        else:
            return False
