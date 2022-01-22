

# def fun():
#     n=1
#     yield n
#
# values= fun()
# print(next(values))

#
# li='vivek'
# print(li[::-1])


# def dectobin(n):
#     arr=[32,16,8,4,2,1]
#     for num in range(len(arr)):
#
#         for j in range(num):
#              if arr[num] + arr[j] == n:
#                  arr=[0,0,0,0,0,0]
#                  arr[num] = 1
#                  arr[j] = 1
#
#
#     return arr
#
# print(dectobin(12))


# A simple Python function to demonstrate
# Polymorphism
#
# def add(x, y, z=0):
#     return x + y + z
#
#
# # Driver code
# print(add(2, 3,5))


# class A:
#     def __init__(self,a):
#         self.a =a
#
#     def __sub__(self, other):
#         return self.a - other.a
#
# v1= A(2)
# v2=A(1)
# v3= v1-v2
# print(v3)
#
# a=4
# b=2
# try:
#     c=a/b
#     print(c)
#
# except Exception as e:
#     print('you have an error ->',e)
# finally:
#     print('vivek')
#

# from abc import  ABC,abstractmethod
#
# class A(ABC):
#     @abstractmethod
#     def method1(self):
#         pass
#
# class B(A):
#     def vivek(self):
#         print('vivek')
#
# ob= B()
# # ob.subclassmethod()

# a=(1,2,3)
# v= [x for x in a]
#
# v.pop()
# v.append(5)
#
# v=tuple(v)
# print(v)


# li=[1,2,3]
# li1=[4,5,6]
# z= list(zip(li,li1))
# print(z)
#
# c= list(zip(*z))
# print(c)

import pickle
c = '232'

# value = c[::-1]

# stack=[x for x in c]
# stack.reverse()
#
# print(stack)
# value = ""
# for i in stack:
#
#     value += i
# print(f'value = {value}')
#
#
# if value == c:
#     print('palindorme')
# else:
#     print('not palindrome')

# def rightmostNonZeroDigit(N, A):
#     # code here
#     temp = 1
#     for i in range(len(A)):
#         temp = temp * A[i]
#
#
#     while temp >0:
#         if temp % 10 == 0:
#             c= temp // 10
#             temp = c
#
#         else:
#             print(temp)
# arr=[10,24,10]
# n=len(arr)
# rightmostNonZeroDigit(n,arr )


# def sumofdigits(n):
#     value = [x for x in str(n)]
#     print(value)
#     c = 0
#     for i in range(len(value)):
#         c+=  int(value[i]) ** len(value)
#     print(c)
#     if c== n:
#         print(f'{n} is a armstrong no.')
#     else:
#         print(f'{n} is not a armstrong no.')
#
# sumofdigits(1543)

# def sumwithoutplus(a,b):
#
#     while b!= 0:
#         c= a&b
#         a= a^b
#         b= c<<1
#     return a
#
#
# print(sumwithoutplus(5,4))

# def insertionsort(arr):
#     for i in range(1,len(arr)):
#         temp=arr[i]
#         j=i-1
#         while(j>=0 and temp<arr[j]):
#             arr[j],arr[j+1] = arr[j+1],arr[j]
#             j=j-1
#         print(arr)
#
# arr=[6,2,4,13,7,9,1,0]
# insertionsort(arr)

# def selectionsort(arr):
#     for i in range(len(arr)):
#         min_index = i
#         for j in range(i+1,len(arr)):
#             if arr[min_index] > arr[j]:
#                 min_index = j
#
#         arr[i],arr[min_index] = arr[min_index],arr[i]
#
#     return arr
#
#
# arr=[6,2,4,13,7,9,1,0]
# print(selectionsort(arr))

# def bubblesort(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1] = arr[j+1],arr[j]
#         print(arr)
#
# arr=[6,2,4,13,7,9,1,0]
# bubblesort(arr)

# def fibo(n):
#     a = 0
#     b = 1
#     temp = 0
#     print(a)
#     for i in range(n):
#         temp = a+b
#         a = b
#         b = temp

#         print(b)

# fibo(10)

# def fact(n):
#     temp = 1
#     if n > 1:
#         for i in range(1, n+1):
#             temp *= i
#         print(temp)
#     elif n == 0:
#         print(0)


# fact(5)

# def perfectno(low, up):

#     for i in range(low, up+1):
#         temp = 0
#         for j in range(1, i):
#             if i % j == 0:
#                 temp += i

#     # return temp

#         if temp == i:
#             print(f'{temp}, is a perfect number')


# print(perfectno(1, 20))


class parent:
    def __init__(self, name):
        self.name = name

    def prin1(self):
        return self.name

    def prin(self):
        return True

    def vi(self):
        print('vivek is good')


class child(parent):

    def prin(self):
        return False


# obj1 = parent('vivek')
# print(obj1.prin(), obj1.prin1())
obj1 = child(12)
print(obj1.prin(), obj1.prin1())
obj1.vi()
# print(obj1.prin())
