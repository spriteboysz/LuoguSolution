#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-20 23:32:18
LastEditTime: 2021-10-21 00:11:52
Description: 求正整数2和n之间的完全数
FilePath: B2127.py
'''


def isPerfect(num):
    factor = [1]
    divisor = 2
    # *num下限值为 **0.5
    while divisor <= num ** 0.5:
        if num % divisor == 0:
            factor.append(divisor)
            factor.append(num // divisor)
        divisor += 1

    if sum(factor) == num:
        return True
    else:
        return False


def func():
    n = int(input())
    for i in range(6, n + 1):
        if isPerfect(i):
            print(i)


if __name__ == '__main__':
    func()
