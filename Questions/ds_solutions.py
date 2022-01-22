def maxproduct(arr, n):
    maxi = 1
    for i in range(n-1):
        for j in range(i+1, n-1):
            new_max = arr[i] * arr[j]
            if new_max > maxi:
                maxi = new_max
                pairs = arr[i], arr[j]
    print(maxi)
    print(pairs)


arr = [2, 10, 20, 9, 5, 7]
n = len(arr)
maxproduct(arr, n)
