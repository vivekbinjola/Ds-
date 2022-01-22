# lower = 10
# upper = 30


# def prime(lower, upper):
#     for num in range(lower, upper+1):
#         # print(num)
#         if num > 1:
#             for j in range(2, num):
#                 if num % j == 0:
#                     break
#             else:
#                 print(num)


# prime(lower, upper)


# lower = 10
# upper = 30
#
# def prime(low,up):
#     for i in range(low,up+1):
#         for j in range(2,i):
#             if i % j == 0:
#                 break
#         else:
#             print(i)
# prime(lower,upper)

# def fact(n):
#     temp = 1
#     for i in range(1,n+1):
#         if i == 0:
#             return 0
#         elif i >=1:
#             temp *= i
#     print(temp)
# fact(5)
#
# low=int(input('enter low range'))
# up = int(input('enter up range'))
#
#
# v= [ int(x) for x in str(digits)]
# print(v)
# total=0
# pow=0
# for i in range(low,up+1):
#     pow=v[i]**len(v)
#     total=pow+total
# print(total)
#
# if(total==digits):
#     print('armstrong')
# else:
#     print('not armstrong')


# def vivek(x):
#     x=8
#     print(id(x))
#     print('x',x)
#
# a=10
# vivek(a)
# print(id(a))
# print('a',a)
#

# f = open(r"C:\Users\NEW\Desktop\python.txt", "r")
# print(f.read(3))
# f.close()


# f = open(r"C:\Users\NEW\Desktop\python.txt", "a")
# f.write('kese hai ap?')
# f.close()
#
#
# f = open(r"C:\Users\NEW\Desktop\python.txt", "r")
# print(f.read())
# f.close()


# f=open(r'C:\Users\NEW\Desktop\python.txt','w')
# f.write('file is being append')
# f.close()
#
# f=open(r'C:\Users\NEW\Desktop\python.txt','r')
# print(f.read())
# f.close()


# f=open('vivek.txt','a')
# f.write('hi ....')
# f.close()
# f=open('vivek.txt','r')
# print(f.read())
# f.close()
# import os
# if os.path.exists(r'vive.txt'):
#     os.remove('vive.txt')
#
# v=open('bin.txt','r')
# (v.read())

# unicode = '\u0123'
# print(unicode)


# def f1():
#     print('f1 called')
#
# def f2(f):
# #      f()
# #
# # if __name__ == '__main__':
# #     f2(f1)
#
#
# # def fibo(n):
# #
# #     if n<2:
# #         return n
# #     else:
# #          return fibo(n-1) + fibo(n-2)
# #
# #
# # print(fibo(9))
#
# def statm(n):
#     if n > 1:
#         c = 1
#         for i in range(2, n + 1):
#             c = n * statm(n - 1)
#
#         return c
#     elif n == 0:
#         return 1
#     else:
#         return -1
#
# statm(6)
#
# class Vivek:
#
#     school="dav"
#
#     def __init__(self,m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#
#     def cl(self):
#         return self.m1
#
#     @classmethod
#     def clsmethod(cls):
#         return cls.school
#
#     @staticmethod
#     def statm(n):
#         if n>1:
#             c=1
#             for i in range(2,n+1):
#
#                  c= c*i
#
#             return c
#         elif n==0:
#             return 1
#         else:
#             return -1
#


# # s1= Vivek(21,23,34)
# print(Vivek.statm(4))
# print(s1.cl())
# print(s1.clsmethod())
# print(Vivek.clsmethod())
#


# class A:

#      def __init__(self):
#          print('vivek')

#      def name1(self):
#          print('1')

#      def lstname1(self):
#         print('2')


# class B():
#     def __init__(self):
#         super().__init__()
#         print("binjola")

#     def name2(self):
#         print('3')

#     def lstname2(self):
#         print('4')

# class C(A,B):

#     def __init__(self):
#         super().__init__()
#         print('vivekbinjola')

# a= C()


# def game_with_number(arr,  n):
#     # Complete the function
#     for i in range(n):
#         if i < n-1:
#             print(arr[i] | arr[i+1])
#         elif i == n:
#             print(arr[i])


# arr = [10, 11, 1, 2, 3]
# n = len(arr)
# print(game_with_number(arr, n))


# def palin(n):
#     digit = n
#     v = ""
#     l = len(n)-1

#     for i in range(l, -1, -1):

#         v = v + n[i]
#     print(v)
#     if v == digit:
#         print('palindrome')


# palin('level')

# def armstrong(l):
#     # v = [x for x in str(l)]
#     # n = 0
#     # for i in range(len(v)):
#     #     n += int(v[i])**len(v)
#     # print(n)
#     v = 0
#     for i in range(len(l)):
#         v += int(l[i]) ** len(l)
#     print(v)


# armstrong('372')

# def digiroot(n):
#     num = [x for x in str(n)]
#     w = 0
#     l = 0
#     for i in range(len(num)):
#         w += int(num[i])
#     # print(w)

#     num1 = [y for y in str(w)]
#     for j in range(len(num1)):
#         l += int(num1[j])
#     return l
#     # print(l)


# print(digiroot(347))

# def digiroot(n):
#     w = 0
#     l = 0
#     for i in range(len(n)):
#         w += int(n[i])
#     print(w)
#     num = str(w)

#     for j in range(len(num)):
#         l += int(num[j])
#     print(l)


# # digiroot('347')

# # def sumofoddint(arr):
# #     j = 2
# #     num = 0
# #     for i in range(len(arr)):
# #         if arr[i] % j != 0:
# #             num += arr[i]
# #     print(num)


# # arr = [1, 4, 6, 7, 10, 12, 11, 5]
# # sumofoddint(arr)


# # def inversionpair(arr):
# #     count = 0
# #     for i in range(len(arr)-1):
# #         for j in range(i+1, len(arr)):
# #             if arr[i] > arr[j]:
# #                 count += 1
# #     print(count)


# # arr = [13, 10, 9, 6, 21, 15, 14]
# # inversionpair(arr)

# class ParentClass:
#     # def __init__(self, a, b):
#     #     self.a = a
#     #     self.b = b
#     #     print('parentclass')

#     def method1(self, a):
#         print('hi parent')

#     def method1(self, a, b):
#         print('hi method second')


# # class SubClass(ParentClass):

# #     # def __init__(self, a1, b1):
# #     #     super().__init__(1, 2)
# #     #     self.a1 = a1
# #     #     self.b1 = b1
# #     #     print('subclass')
# #     #     print(f'{self.a}')

# #     # def method1(self):
# #     #     print(f'hello child')
# #     pass


# v1 = ParentClass()
# # v2 = SubClass()
# v1.method1(1)
# v1.method1(1, 2)

# def armstrong(low, up):
#     for i in range(low, up+1):
#         temp = 0
#         num = i

#         while num > 0:
#             digit = num % 10
#             temp += digit**3
#             num //= 10

#             if temp == i:
#                 print(i)


# print(armstrong(100, 200))


# def add(x, y):
#     while(y != 0):
#         digit = x & y
#         x = x ^ y
#         y = digit << 1
#     return x


# print(add(4, 5))


# def prime(low, up):
#     for i in range(low, up+1):
#         if i > 1:
#             for j in range(2, i):
#                 if i % j == 0:
#                     break
#             else:
#                 print(f'prime{i}')


# prime(10, 20)

# def leapyear(n):
#     if n % 4 == 0:

#     else:
#         if n % 100 != 0 and n % 4 == 0:
#             print('leap year')
#         elif n % 100 == 0 and n % 400 != 0:
#             print(' leap year')
#         else:
#             print('not a leap year')


# leapyear(2021)

# def getMinMax(a, n):
#     min = a[0]
#     max = a[0]
#     for i in range(n):
#         if a[i] < min:
#             min = a[i]
#             print(f'min= {min}')
#         if a[i] > max:
#             max = a[i]
#     print(f'max= {max}')


# arr = [4, 1, 8, 9, 13, 12, 14, 7]
# n = len(arr)
# getMinMax(arr, n)
# Python program to print first half in
# ascending order and the second half
# in descending order


# function to print half of the array in
# ascending order and the other half in
# descending order
def printOrder(arr, n):

    # sorting the array
    arr.sort()

    # printing first half in ascending
    # order
    i = 0
    while (i < n / 2):
        print(arr[i], end=''),
        i = i + 1

    # printing second half in descending
    # order
    j = n - 1
    while j >= n / 2:
        print(arr[j], end=''),
        j = j - 1


# Driver code
arr = [5, 4, 6, 2, 1, 3, 8, 9, 7]
n = len(arr)
printOrder(arr, n)

# This code is contributed by Nikita Tiwari.
