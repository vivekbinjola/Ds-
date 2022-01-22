'''def vivek(n):
    if n < 1:
        print('n is printed')
    else:
        vivek(n-1)
        print('print delay', n)


vivek(4)


def vivekPower(n):
    if n == 0:
        return 1
    else:
        power = vivekPower(n-1)
        return power * 2


vivekPower(3)

# Factorial

def factorial(n):
    assert n >= 0 and n == int(n), 'Input should be a positive integer'
    if n == 0:
        return 1
    else:

        fact = n * factorial(n-1)
        return fact


print(factorial(15))

# Fibonacci Series


def Fibonacci(n):
    assert n >= 0 and n == int(
        n), 'Fibonacci number cannot be negative or decimal number'
    if n in [0, 1]:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


print(Fibonacci(5))


def sumOfDigits(n):
    assert n >= 0 and int(n) == n, 'Number should be positive integer '
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumOfDigits(int(n/10))


print(sumOfDigits(35411)) 


def power(x, n):
    assert n >= 0 and int(n) == n, 'Power should be a positive integer'
    if n == 0:
        return 1
    else:
        return x * power(x, n-1)


print(power(-10, 4))'''


def GCD(x, y):
    if y == 0:
        return x
    else:
        return GCD(y, x % y)


print(GCD(16, 10))
