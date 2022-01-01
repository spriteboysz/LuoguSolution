#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-10 13:54:28
LastEditTime: 2021-10-14 00:18:51
Description: 口算练习题
FilePath: P1957.py
'''


def func():
    n = int(input())
    for i in range(n):
        row = input().strip().split()
        if len(row) == 3:
            symbol, a, b = row
        else:
            a, b = row

        if symbol == "a":
            s = a + "+" + b + "=" + str(int(a) + int(b))
        elif symbol == "b":
            s = a + "-" + b + "=" + str(int(a) - int(b))
        elif symbol == "c":
            s = a + "*" + b + "=" + str(int(a) * int(b))

        print(s)
        print(len(s))


if __name__ == '__main__':
    func()
