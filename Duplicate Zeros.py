class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        c = []
        for i in range(len(arr)):
            if len(c) < len(arr):
                if arr[i] == 0:
                    c.append(arr[i])
                    if len(c) < len(arr):
                        c.append(arr[i])
                else:
                    c.append(arr[i])
        for i in range(len(arr)):
            if len(arr) == len(c):
                arr[i]=c[i]