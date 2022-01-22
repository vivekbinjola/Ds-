# List is implemented a dynamic array

#        O-complexity
#   Looking by index = O(1) -constant time operation
#  Looking by value = O(n) - n is the no. of iterations.
#  Array traversal(to get whole array) = O(n)
# inserting new element at any index = O(n)
# Array deletion =O(n)

# Dynamic array-
# ArrayList<Integer> stockPrices = new ArrayList<Integer>();

# Initial capacity =10;
# after the capacity is full initial array is copied & pasted into new array with new capacity.
# Additional capacity = initial *2
#
# question 1
# .Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,
#
# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
#
# array = [2200, 2350, 2000, 2130, 2190]
# newarray=array[1]-array[0]
# quarterly_expenses = array[0]+array[1]+array[2]
# array.append(1980)
#
# array[3]= array[3]-200
# print(f' difference between feb & jan is {newarray}')
#
# print(f' total expense in first quarter {quarterly_expenses} ')
#
# for i in range(len(array)):
#     if array[i]== 2000:
#         print(f' array[{i}] has expenses equals to= {array[i]}')
#
#
# print(f'adding june month,new expenses = {array}')
# print(f'corrected array after refund in april={array}')
#
#
# question 2.
# You have a list of your favourite marvel super heros.
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,
#
# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
#
#
# heroes=['spider man','thor','hulk','iron man','captain america']
#
# v=len(heroes)
# print(v)
#
# heroes.append('black panther')
# print(heroes)
#
# heroes.pop(5)
# heroes.insert(3,'black panther')
# print(heroes)
#
# heroes[1:3] = ['doctor strange']
# print(heroes)
#
# heroes.sort()
# print(heroes)

#
# question 3.Create a list of all odd numbers between 1 and a max number.
# Max number is something you need to take from a user using input()
# function


import numpy as np
arr1 = [1, 2, 3, 4, 5]


arr = np.array([
    [1, 2, 3, 4],
    [2, 3, 5, 4],
    [2, 3, 5, 4],
    [2, 3, 5, 4]])

'''
from array import *

arr = array('i', [1, 2, 3, 4])
arr1 = array('i', [1, 2, 3, 4, 5, 6])


# print(arr[3])


def traversearray(array):
    for i in array:
        print(i)


traversearray(arr)


def indice(array, index):
    if index >= len(array):
        print('index out of range')
    else:
        print(array[index])


indice(arr, 5)


def search(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return 'element does not exist'


print(search(arr, 2))
print(67*12)

arr.remove(4)
print(arr)


        insertion in 2D array
        
# newArr = np.insert(arr, 0, [[4, 4, 5, 6]], axis=0) axis = 0 for adding row
# newArr = np.insert(arr, 0, [[4, 4]], axis=1) axis = 1 for adding column

newArr = np.append(arr, [[4, 4, 6, 7]], axis=0)
print(newArr)

        Accessing specific element in 2d array


def accessnum(array, rowindex, colindex):
    if colindex >= len(array[0]) and rowindex >= len(array):
        print('Give proper Row/Column index')
    else:
        print(array[rowindex][colindex])


print(arr)
accessnum(arr, 2, 2)

        Traverse 2d array


def traverse2darr(array):
    for i in range(len(array)):         Timecomplexity:m*n
        for j in range(len(array)):
            print(array[i][j])


print(arr)
traverse2darr(arr)


def search2dnum(array, value):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j] == value:
                print(f'this is the index {i},{j}')


print('value not found in the given array')


print(arr)
search2dnum(arr, 1)


        # delete row/col from 2d array
deletearr = np.delete(arr, 1, axis=1)
print(arr)
print(deletearr)'''
print("Hello World")
