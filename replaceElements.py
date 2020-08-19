class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1,-1,-1):
            
            if i == (len(arr)-1):
                temp1 = arr[i]
                arr[i] = -1
                
            elif i == (len(arr)-2):
                temp2 = arr[i]
                arr[i] = temp1
                if temp2 < temp1:
                    temp2 = temp1
                
            else:
                temp3 = arr[i]
                arr[i] = temp2
                if temp2 < temp3:
                    temp2= temp3
        return arr