#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-28 23:26:18
LastEditTime: 2022-01-02 21:37:18
Description: 最大公约数和最小公倍数问题
FilePath: P1029.py
'''


from math import gcd


def func():
    x, y = map(int, input().strip().split())
    count = 0
    flag = 0
    for i in range(1, int((x * y) ** 0.5) + 1):
        if (x * y) % i == 0 and gcd(i, (x * y) // i) == x:
            count += 1
            if i * i == x * y:
                flag = 1

    print(count * 2 - flag)


if __name__ == '__main__':
    func()
