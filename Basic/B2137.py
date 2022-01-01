#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-21 23:37:59
LastEditTime: 2021-12-11 22:01:08
Description: 判断素数个数
FilePath: B2137.py
'''


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def func():
    x, y = sorted(map(int, input().strip().split()))
    count = 0
    for i in range(x, y + 1, 1):
        if isPrime(i):
            count += 1
    return count


if __name__ == '__main__':
    ans = func()
    print(ans)
