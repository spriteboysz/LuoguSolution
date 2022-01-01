#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-09-26 21:24:26
LastEditTime: 2021-09-26 21:30:09
Description: 整数的个数
FilePath: B2061.py
'''


def func():
    count = int(input())
    nums = list(map(int, input().strip().split()))

    k1 = k5 = k10 = 0

    for i in range(count):
        if nums[i] == 1:
            k1 += 1
        elif nums[i] == 5:
            k5 += 1
        elif nums[i] == 10:
            k10 += 1

    print(k1)
    print(k5)
    print(k10)


if __name__ == '__main__':
    func()
