#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-30 22:21:07
LastEditTime: 2021-10-30 22:42:04
Description: 阶乘数码
FilePath: P1591.py
'''


def factorial(num, lst):
    lst.extend([0] * (num - len(lst) + 1))
    for i in range(2, num + 1):
        lst[i] = lst[i - 1] * i


def func():
    t = int(input())

    lst = [0, 1]
    for _ in range(t):
        n, a = map(int, input().strip().split())
        if n > len(lst) - 1:
            factorial(n, lst)

        print(str(lst[n]).count(str(a)))


if __name__ == '__main__':
    func()
