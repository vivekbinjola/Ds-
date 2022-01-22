arr = [3, 1, 5, 9, 7, 4, 8]
'''
#BubbleSort
def BubbleSort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    print(arr)
#space complexity - o(1)
#time complexity - o(n**2)  

BubbleSort(arr)

# Selection sort
array = [3, 1, 5, 9, 7, 4, 8]


def selectionsort(arr):
    for i in range(len(arr) - 1):
        min_index = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)


selectionsort(array)

# insertion sort
array = [3, 1, 5, 9, 7, 4, 8]
# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i-1
		while j >=0 and key < arr[j]:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key
	print(arr)

insertionSort(array)'''

# import numpy as np
#
# arr= np.array([5,3,6,8,2,7,1])
#
# for i in range(1,len(arr)):
#     start= arr[i]
#     j=i-1
#     while(j>=0 and arr[j]>start):
#         arr[j+1] = arr[j]
#         j=j-1
#
#     arr[j+1] = start
#     print(arr)





