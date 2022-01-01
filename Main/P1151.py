#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-22 10:23:45
LastEditTime: 2021-10-22 10:36:07
Description: 子数整数
FilePath: P1151.py
'''


def func():
    k = int(input())

    flag = False
    for i in range(10000, 30001):
        sub1, sub2, sub3 = int(str(i)[:3]), int(str(i)[1:4]), int(str(i)[2:])
        if sub1 % k == 0 and sub2 % k == 0 and sub3 % k == 0:
            flag = True
            print(i)

    if not flag:
        print("No")


if __name__ == '__main__':
    func()
