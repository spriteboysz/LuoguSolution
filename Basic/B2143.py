#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-10 22:31:01
LastEditTime: 2021-12-10 23:50:25
Description: 进制转换
FilePath: B2143.py
'''


def func():
    base = ["0", "1", "2", "3", "4", "5", "6", "7",
            "8", "9", "A", "B", "C", "D", "E", "F"]
    x, m = map(int, input().strip().split())
    num = ""
    while True:
        div, mod = divmod(x, m)
        num += base[mod]
        if div != 0:
            x = div
        else:
            break
    print(num[::-1])


if __name__ == '__main__':
    func()
