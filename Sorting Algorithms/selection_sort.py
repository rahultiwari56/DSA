# https://www.geeksforgeeks.org/selection-sort/

def for_loop(arr):
    for i in range(len(arr)):
        s=i
        for j in range(i+1, len(arr)):
            if arr[s]>arr[j]:
                s=j

        arr[s],arr[i]=arr[i],arr[s]

    return arr


def while_loop(arr):

    i = 0
    arr_len = len(arr)

    while i<arr_len:
        s=i
        for j in range(i+1, len(arr)):
            if arr[s]>arr[j]:
                s=j
        arr[s],arr[i]=arr[i],arr[s]
        i+=1
        
    return arr


if __name__=='__main__':
    arr = [25,5,42,24,22,-2,11]
    # res = for_loop(arr)
    res = while_loop(arr)
    print(res)