#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-04 23:00:52
LastEditTime: 2021-12-04 23:08:44
Description: 三连击（升级版）
FilePath: P1618.py
'''


def func():
    a, b, c = map(int, input().strip().split())
    flag = False
    for i in range(123, 1000 * a // c):
        if i * b % a == 0 and i * c % a == 0:
            num = str(i) + str(i * b // a) + str(i * c // a)
            if len(set(list(num))) == 9 and "0" not in num:
                flag = True
                print(i, i * b // a, i * c // a)
    if not flag:
        print("No!!!")


if __name__ == '__main__':
    func()
