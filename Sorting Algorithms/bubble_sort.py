

def for_loop(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def while_loop(arr):

    i = 0
    arr_len = len(arr)

    while i<arr_len:
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

        i+=1
        
        
    return arr


if __name__=='__main__':
    arr = [25,5,42,24,22,-2,11]
    res = for_loop(arr)
    # res = while_loop(arr)
    print(res)