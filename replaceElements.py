def num(arr):
    for i in range(len(arr)):
        
        if i == len(arr)-1:
            arr[i] = -1
            return arr
        length = i + 1
        maxx = max(arr[length:])
        arr[i]= maxx
    return arr