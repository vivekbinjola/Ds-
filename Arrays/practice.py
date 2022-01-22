from array import *
import math
a = [1, 2, 3, 4, 5, 6, 7]

'''class Student:
    def vivek(self, name, classname):
        self.name = name
        self.classname = classname
        print(name,  classname)


var = Student()

var.vivek('vivek', 12)


class car:
    def __init__(self, modelname, year):
        self.modelname = modelname
        self.year = year

    def display(self):
        print(f'{self.salary}self.modelname, self.year')


c1 = car("Toyota", 2016)
c1.salary = 10999
c1.display()

        # Linear Search




def traverse(array, n):
    for i in range(len(array)):
        if array[i] == n:
            return i

    return 'no such element is in the array'


print(traverse(a, 5))
print(len(a))

# Binary Search - works only with sorted arrays
# Time complexity - o(logn) -o(1)


def binarysearch(array, value):
    start = 0
    end = len(array)-1
    middle = math.floor((start + end)/2)
    print(start, middle, end)

    while not(array[middle] == value) and end >= start:
        if array[middle] > value:
            end = middle - 1

        else:
            start = middle + 1
        middle = math.floor((start + end)/2)
        print(start, middle, end)

    if array[middle] == value:
        return middle
    else:
        return -1


print(binarysearch(a, 7))

# a = [1, 2, 3, 4, 5, 6, 7]
#      S         M        E
#      S  M  E
#            SEM

# arr =[1,3,2,8,4]
# arr.sort()
# print(arr)
'''
# array = [1, 2, 3, 9, 5, 8, 7]
#
#
# def reversearr(arr):
#     start = 0
#     end = len(arr)-1
#
#     while (arr[start] < arr[end]):
#         arr[start], arr[end] = arr[end], arr[start]
#         start = start + 1
#         end = end - 1
#     print(arr)
#
#
# reversearr(array)

import numpy as np
import random


di = {1: "X", 2: "O"}

index = {1: ([0], [0]), 2: ([0], [1]), 3: ([0], [2]), 4: ([1], [0]), 5: ([1], [1]), 6: ([1], [2]), 7: ([2], [0]),
         8: ([2], [1]), 9: ([2], [2])}


def show_board(arr):
    print("                ")
    print(arr[0][0], " | ", arr[0][1], " | ", arr[0][2])
    print("---------------")
    print(arr[1][0], " | ", arr[1][1], " | ", arr[1][2])
    print("---------------")
    print(arr[2][0], " | ", arr[2][1], " | ", arr[2][2])
    print("                ")


def win_checker(arr):
    # Checking Rows for X.
    if ((arr[0][0] + arr[0][1] + arr[0][2]) == "XXX") or ((arr[1][0] + arr[1][1] + arr[1][2]) == "XXX") or (
            (arr[2][0] + arr[2][1] + arr[2][2]) == "XXX"):
        return "X"
    # Checking Rows for O.
    elif ((arr[0][0] + arr[0][1] + arr[0][2]) == "OOO") or ((arr[1][0] + arr[1][1] + arr[1][2]) == "OOO") or (
            (arr[2][0] + arr[2][1] + arr[2][2]) == "OOO"):
        return "O"
    # Checking Cols for X.
    elif ((arr[0][0] + arr[1][0] + arr[2][0]) == "XXX") or ((arr[0][1] + arr[1][1] + arr[2][1]) == "XXX") or (
            (arr[0][2] + arr[1][2] + arr[2][2]) == "XXX"):
        return "X"
    elif ((arr[0][0] + arr[1][0] + arr[2][0]) == "OOO") or ((arr[0][1] + arr[1][1] + arr[2][1]) == "OOO") or (
            (arr[0][2] + arr[1][2] + arr[2][2]) == "OOO"):
        return "O"
    elif arr[0][0] + arr[1][1] + arr[2][2] == "XXX":
        return "X"
    elif arr[0][0] + arr[1][1] + arr[2][2] == "OOO":
        return "O"
    elif arr[0][2] + arr[1][1] + arr[2][0] == "XXX":
        return "X"
    elif arr[0][2] + arr[1][1] + arr[2][0] == "OOO":
        return "O"


li = []

n = 0


def singleplayer(mat):
    i = 1
    while win_checker(mat) != "X" or win_checker(mat) != "O":

        if i % 2 != 0:
            p = int(input("Player X turn: "))
            if p not in li:
                mat[index[p]] = di[1]
                i += 1
                show_board(mat)
                li.append(p)
            else:
                print("You can't enter at occupied place")

        if i % 2 == 0:
            a = random.randint(1, 9)
            if a not in li:
                mat[index[a]] = di[2]
                i += 1
                show_board(mat)
                li.append(a)

        if win_checker(mat) == "X":
            print("player X wins.")
            break
        elif win_checker(mat) == "O":
            print("player O wins.")
            break
        elif i == 10 and win_checker(mat) != "X" and win_checker(mat) != "O":
            print("Match Tied..")
            break
    menu()


def multiplayer(mat):
    i = 1
    while win_checker(mat) != "X" or win_checker(mat) != "O":
        if i == 10 and win_checker(mat) != "X" and win_checker(mat) != "O":
            print("Match Tied..")
            break
        elif win_checker(mat) == "X":
            print("player X wins.")
            print("              ")
            break
        elif win_checker(mat) == "O":
            print("player O wins.")
            print("              ")
            break
        else:
            if i % 2 != 0:
                n = int(input("Player 1 turn: "))
                if n not in li:
                    mat[index[n]] = di[1]
                    i += 1
                    show_board(mat)
                    li.append(n)


                else:
                    print("You can't enter at occupied place")

            # elif i == 10 and win_checker(mat) != "X" and win_checker(mat) != "O":
            #    print("Match Tied..")
            #    break

            elif i % 2 == 0:
                n = int(input("Player 2 turn: "))
                if n not in li:
                    mat[index[n]] = di[2]
                    i += 1
                    show_board(mat)
                    li.append(n)

                else:
                    print("You can't enter at occupied place")

    menu()


def menu():
    li.clear()
    board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    board = np.array(board).reshape(3, 3)
    print("=" * 20)
    print("Welcome to Tic Tac Toe game.")
    print("1. MultiPlayer")
    print("2. SinglePlayer")
    print("3. Quit.")
    print("=" * 20)
    ch = input("Enter your choice: ")
    if ch == "1":
        show_board(board)
        print("Enter block no where you want to enter: ")
        multiplayer(board)
    elif ch == "2":
        show_board(board)
        singleplayer(board)
    elif ch == "3":
        print("Have a nice day Bye...")
        exit()
    else:
        print("Invalid Input Please select from given choices and try again.")
        menu()


menu()