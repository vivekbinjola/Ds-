def insertionSort(arr):
    for i in range(1, len(arr)):
        temp = a[i]
        j = i-1
        while j > 0 and temp > arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        temp = arr[j+1]
    return arr


arr = [6, 4, 1, 2, 9]
print(insertionSort(arr))
