#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-08 21:59:34
Description: 回文质数
FilePath: P1217.py
'''


import time


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def func():
    a, b = sorted(map(int, input().strip().split()))
    for i in range(a, b + 1):
        if len(str(i)) % 2 == 0 and i != 11:
            continue
        elif i % 2 == 0:
            continue
        elif str(i) == str(i)[::-1] and isPrime(i):
            print(i)


if __name__ == '__main__':
    start = time.time()
    func()
    end = time.time()
    print(end - start)
