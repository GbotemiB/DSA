class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        for i in range(len(A)):
            if len(A) > 2:
                max_integer = max(A)
                max_index = A.index(max_integer)
                A_array1 = A[:A.index(max(A))+1]
                A_array2 = A[A.index(max(A)):]
                if len(A_array1) > 1 and len(A_array2) > 1:
                    for i in range(len(A_array1)-1):
                        if A_array1[i] < A_array1[i+1]:
                            pass
                        else:
                            return False
                    for i in range(len(A_array2)-1):
                        if A_array2[i] > A_array2[i+1]:
                            pass
                        else:
                            return False
                    return True
                else:
                    return False