import math
import random
import os
import copy


def testFunction1():
    x = 1
    y = 2
    if x > y:
        print("x")
    elif x == y:
        print("=")
    else:
        print("y")


# 斐波那契数列
known = {0: 0, 1: 1}


def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n - 1) + fibonacci(n - 2)
    known[n] = res
    return res


# 阶乘,同时判断是否符合整数Integer
def factorial(n):
    if not isinstance(n, int):
        print('Factorial is not defined for Integers.')
    elif n < 0:
        print('Factorial is not defined for Integers.')
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# 直方图
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


# 翻转直方图
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def test1():
    # do nothing
    print(os.getcwd())
    print(os.path)
    print(os.path.isdir('pdf'))
    print(os.path.exists('pdf'))
    print(os.path.isfile('pdf'))
    print(os.listdir(os.getcwd()))


class Time:
    """
    Represents the time of day.
    """

    def __init__(self, hour, minute, second):
        self.second = second
        self.minute = minute
        self.hour = hour

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def print_time(self):
        print("%.2d:%.2d:%.2d" % (self.hour, self.minute, self.second))



#生成器表达式
def avoids(word, forbidden):
    return not any(letter in forbidden for letter in word)

