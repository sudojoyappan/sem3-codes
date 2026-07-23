def quicksort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr.pop()
    less=[]
    high=[]
    for i in arr:
        if i<pivot:
            less.append(i)
        else:
            high.append(i)
    return quicksort(less)+[pivot]+quicksort(high)

arr = [38, 27, 43, 3, 9, 82, 10]

print(quicksort(arr))