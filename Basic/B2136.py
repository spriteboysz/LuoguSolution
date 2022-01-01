#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-11 22:01:43
LastEditTime: 2021-12-11 22:08:55
Description: 素数回文数的个数
FilePath: B2136.py
'''


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def func():
    n = int(input())
    if n < 11:
        return 0
    elif n == 11:
        return 1
    else:
        count = 1
        for i in range(12, n + 1):
            if len(str(i)) % 2 == 0:
                continue
            if str(i) == str(i)[::-1] and isPrime(i):
                count += 1
        return count


if __name__ == '__main__':
    ans = func()
    print(ans)
