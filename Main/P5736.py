#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-31 22:14:28
LastEditTime: 2021-12-05 17:03:38
Description: 质数筛
FilePath: P5736.py
'''


def isPrime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        else:
            return True


def func():
    n = int(input())
    lst = list(map(int, input().strip().split()))
    lst2 = list(filter(isPrime, lst))
    print(" ".join(map(str, lst2)))


if __name__ == '__main__':
    func()
