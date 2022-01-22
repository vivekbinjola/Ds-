'''#print('hello')

 
#x,y,z=(2,3,4)
#print(x,y,z)

#a=x+y
#print(a)

#Casting

#x= float(x)
#print(type(x),x)

#String formatting
 
 #f-strings
#name ='vivek'
#age=34

#print(f'my name is {name} and age is {age}')

#String Methods

#s='vivekbinjola'

#capitalize string

#print( s.capitalize())

#A list is a collection which ils ordered and changeable .Allows duplicate members.

#Create list 
#numbers =[1,2,3,4]
#fruits = ['apples','oranges','grapes','pears']
 

#fruits.append('mangoes')
 
 
#fruits.insert(2,'banana')
#fruits.remove('oranges')
#fruits.pop(1)
#fruits.sort()
#fruits.reverse()
#reverse sort
#fruits.sort(reverse=True)
#fruits[0]='peaches'
#print(fruits)


#Tuple(immutable)-duplicate members

#create tuple
fruits=('apple','orange','peach','mango')
 
#print( fruits)
#deleting a tuple
 

 
#Set-no duplicate members
fruits_set = {'apples','oranges','mango'} 

#print('oranges' in fruits_set)


#fruits_set.remove('apples')
#print(fruits_set) 

fruits_set.add('mango')
#print(fruits_set)

#Dictionary is a collection  which is unordered,changeable and indexed.
#no duplicate member
person={
    'first_name':'john',
    'last_name':'doe',
    'age':39
}
##print(person['first_name'])
#print(person,type(person))

#Add value
#person['phone']='89342424234'
#print(person)

#dict keys
#print(person.keys())

#dict items
#print(person.items())

#copy dictionary
#person2=person.copy()
#person2['city']='Dehradun'
#print(person2)

#remove item
#del person['age']
#person.pop('phone')
#print(person)

#list of dictionaries
##persons=[
  #  {'name':'vivek' ,'age':34},
  #  {'name':'sonali' ,'age':24}

#]

#print(persons[1]['age'])


#Functions-is a block of code which runs when it is called
#print('hello')

#def sayHello(name):
  # print(f' {name}')

#sayHello('vivek')
def getSum(num1,num2):
    total= num1+num2
    return total
print(getSum(6,4))

  #Lamda function is a small anonymous function.
  #it can take any number of arguments,but can only have
  #one expression just like arrow function in js.

getvalue= lambda num1,num2 : num1+ num2
print(getvalue(23,4))

#Conditionals
x=3
y=5
#if-else
#comparison operators
if x>y:
  print(f'{x}is greater than {y}')

elif x==y:
  print(f'{x}is equals to {y}')

else:
  print(f'{x}is smaller than {y}')
 
#logical operators(and,or,not)

#Membership operators(in,not in)-used to determine wheather
#a value is present in an object or not.

numbers=[1,2,3,4,5]

if x in numbers:
  print(f'{x} is present in numbers ')

if x not in numbers:
  print(f'{x} is not present in numbers ')

#Identity operators(is,is not)-to compare objects,to check wheather they are
# same object with same memory location or not.

if x is y:
  print(x is y)

if x is not y:
  print(x is not y)

#Loops
#for loop
people=['vivek','ankit','palak','aniket']

#for person in people:
 # print(f'person:{person}')

 
#for person in people:
  #if person== 'palak':
  # break
  #print(f'person:{person}')

for person in people:
  if person== 'palak':
    continue
  print(f'person:{person}')

for i in range(len(people)):
  print({people[i]})

for i in range(0,10):
  print({i})

#while

count=0

while count<=10:
  print(f'count:{count}')

  count +=1

#Module- it is basically a file containing a set of functions
#to include in your applications.

import datetime
import time
 
today=datetime.date.today()
timestamp=time.time()
print(today)
 
# A classs is like a blueprint for creating objects.
#  An object has properties and methods (functions) associated with it.
#Almost everything in python is an object

#Create class
class Vivek:
  
  def __init__(self,name,age):
    self.name = name
    self.age = age

  def vixen(self):
    return f'my name is {self.name} and age is {self.age}'

  def aged(self):
    self.age +=1

v = Vivek('vivek', 20)
v.aged()
print(v.vixen())

#Extend class
class customer(Vivek):
  def __init__(self,name,age):
    self.name = name
    self.age = age

  def set_balance(self,balance):
    self.balance=balance

  def vixen(self):
    return f'my balance is {self.balance}'



var=customer('palak','19')
var.set_balance(200)
print(var.vixen())


 var="vivek binjola"
print(var[::-1])

li=[2,3,4,5,6]
print(min(li))
 

#File -python has functions for creating ,reading
#updating and deleting files.

#opening a file

myfile=open('myfile.txt','w')

#get some info
print('Name: ',myfile.name)
print('is closed: ',myfile.closed)
print('opening mode: ',myfile.mode)

#write to file
myfile.write('i love python')
myfile.write(' and js')
myfile.close()
print('is closed: ',myfile.closed)

#Append
myfile=open('myfile.txt','a')
myfile.write(' ,i also like PHP')
myfile.close()

#read from a file
myfile=open('myfile.txt','r+')
text=myfile.read(200)
print(text)

               #JSON


import json

#sample json
userjson = '{"name":"vivek", "last_name":"binjola", "age": 21}'

#parse to dictionary(JSON to dict)
var=json.loads(userjson)

print(var)
print(var['name'])

#dictionary to JSON
car={"name":"mustang","year":1947,"model":"btc"}

let=json.dumps(car)
print(let)

         #Math module

import math #or import math as m 
#or from math import sqrt,pow

x = math.sqrt(25)
print(x)


x = math.floor(2.7) #value decreases to lower number
print(x)

x = math.ceil(2.7) #value increases to higher number
print(x)

x = math.factorial(4)
print(x)

print(math.pow(3,2)) #for power numbers

print(math.pi)'''

'''Python’s print() function comes with 
a parameter called ‘end’. By default, the value of 
this parameter is ‘\n’,  i.e. the new line character.

                  #patterns


for j in range(4): 

    for i in range(4):
     print('#',end='')
    print()


for j in range(4): 

    for i in range(j+1):
     print('#',end='')
    print() 

for j in range(4): 

    for i in range(4-j):
     print('#',end='')
    print() 

vivek=[23,35,15,37,75]

for num in vivek:
  if num%2 == 0:
   print(num)
   break
else:
 print('not found') 

                #Pass


  It is used when u have to skip something and
 return to it later if u r not sure

 for eg:-
 
 def func():
 pass

so it will not work and just skip this part
  
             #prime no.

num =7

for i in range(2,num):
  
  if num% i==0:
   print("not prime")
   break

else:
 print("prime")

from array import *
                 # Arrays


val = array('i', [3, 4, 5, 6])

# print(val.buffer_info())
# val.reverse()
# print(val)

for i in range(len(val)):
    print(val[i])
    # or
for e in val:
    print(e)


newarray = array(val.typecode, (a*a for a in val))
print(newarray)'''


def vivekPower(n):
    if n == 0:
        return 1
    else:
        power = vivekPower(n-1)
        return power * 2


vivekPower(3)
