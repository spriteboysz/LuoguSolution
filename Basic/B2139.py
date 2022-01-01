#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-10 23:09:57
LastEditTime: 2021-12-10 23:45:08
Description: 区间内的真素数
FilePath: B2139.py
'''


def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def func():
    m, n = map(int, input().strip().split())
    lst = []
    for i in range(m, n + 1):
        if isPrime(i):
            num = int(str(i)[::-1])
            if isPrime(num):
                lst.append(i)
    if len(lst) == 0:
        print("No")
    else:
        print(",".join(map(str, lst)))


if __name__ == '__main__':
    func()
