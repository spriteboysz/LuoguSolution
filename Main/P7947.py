#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-02 22:39:26
LastEditTime: 2022-01-02 23:00:50
Description: 铝锤制作
FilePath: P7947.py
'''


def func():
    n, k = map(int, input().strip().split())
    factor = []
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                factor.append(i)
                n = n // i
                break

    length = k - sum(factor)
    if length >= 0:
        factor.extend([1] * length)
        print(len(factor))
        print(" ".join(map(str, factor)))
    else:
        print(-1)


if __name__ == '__main__':
    func()
    
