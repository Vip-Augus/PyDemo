import math

def testFunction1():
    x = 1
    y = 2
    if x > y:
        print("x")
    elif x == y :
        print("=")
    else:
        print("y")


def factorial(n):
    if not isinstance(n, int):
        print('Factorial is not defined for Integers.')
    elif n < 0:
        print('Factorial is not defined for Integers.')
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(-2))