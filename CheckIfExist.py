class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        x=(arr)
        for i in range(len(x)):
            for j in range(len(x)):

                if i == j:
                    pass
                else:

                    if (x[i]*2==x[j]) or (x[j]*2==x[i]):
                        print(i,j)
                        return True
        return False