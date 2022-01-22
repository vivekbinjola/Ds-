# to check odd even

# def check(n):
#     if n % 2 == 1:
#         print('Number is odd')
#     else:
#         print('Number is even')
#
# check(3246)

# to check no. is greater than 0

# def check(n):
#     if n > 0 :
#         print('no is positive')
#     elif n == 0:
#         print('no is equal to 0')
#     else:
#         print('no is negative')
#
# check(0)

# check prime number

# def check(n):
#      for i in range (2,n):
#           if n % i == 0:
#                print('Not prime')
#                break
#           else:
#                print('prime')
#                break
#
# a= int(input('Enter the Number:'))
# check(a)

#print all prime numbers
# n=int(input('Enter the Range:'))
#
# for num in range(0,n+1):
#      if num>1:
#           for j in range(2,num):
#                if num%j == 0:
#                     break
#           else:
#                print(num)

#factorial
# def check(n):
#      fact =1
#      if n>0:
#           for i in range(1,n+1):
#                fact = fact * i
#           print(fact)
#      elif n == 0:
#           print(1)
#      else:
#           print('no negative numbers allowed')
# n= int(input('enter the number'))
#
# check(n)
#
# def check(n):
#      assert n>0 and int(n) == n,'negative values not allowed'
#      if n in [0,1]:
#           return 1
#
#      else:
#           return n* check(n-1)
# print(check(0))

# def multiply(n):
#
#      for i in range(1,11):
#           num = n*i;
#           print(f'{n}*{i}= {num}')
# multiply(10)

#fibonacci
# def fibonacci(n):
#     x,y,z= 0,1,0
#     if n <0:
#         print('only positive int. allowed')
#     if n == 0:
#         print(z)
#     while z<n:
#         print(z)
#         x =y
#         y=z
#         z=x+y
#
# fibonacci(30)


# Armstrong Number
# n= int(input('enter the no.'))
# digits = n
# v= [int(x) for x in str(digits)]
# print(v)
# z=0
# c=0
# for i in range(0,len(v)):
#     c= v[i]**len(v)
#     z=z+c
#
# print(z)
# if(z==digits):
#     print("armstrong no.")
# else:
#     print('not armstrong')

#ALT
# n=int(input('enter the number'))
# number = n
# str = len(str(n))
# sum =0
# print(str)
# while(number>0):
#     digit = number % 10
#     sum += digit ** str
#     number = number // 10
#
# if(sum == n ):
#     print(f'{n} is a Armstrong number')
# else:
#     print('Not a Armstrong number')

#armstrong in interval
# lower = int(input("Enter lower range: "))
# upper = int(input("Enter upper range: "))
#
# for num in range(lower, upper + 1):
#     sum = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** 3
#         temp //= 10
#         if num == sum:
#             print(num)

# v= 5**3
# # print(v)
# from array import *
# arr=array('i',[1,2,3,4])
# print(arr[3])
#
# arr.pop(1)
# print(arr)

#
# from queue import Queue
# q=Queue(maxsize=4)
# q.enqueue(1)
# print(q)

# print all natural no.s
# lower= int(input('enter  range'))
#
# def natural(lower):
#     assert lower>0 ,'n should be greater tha 0'
#     sum =0
#
#     while(lower>0):
#         sum += lower
#         lower -= 1
#     print(sum)
#
# natural(lower )

#Leap year 
# n= int(input('enter the year'))
# if n%400 == 0:
#     print('leap year')
#
# else:
#     if n % 4 == 0 and n % 100 != 0:
#         print('leap year')
#     else:
#         print('not a leap year')

#Palindrome
# n = input('enter a string')
# reverse = n[::-1]
# if(reverse == n):
#     print('palindrome')
# else:
#     print('Not a palindrome')
#

n= input('enter a string')
try:
    while(len(n)>0):

        n=n-1
    print(n)
except:
    print('invalid')


