#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-06 15:19:00
LastEditTime: 2021-11-06 22:00:33
Description: Chewbaсca and Number
FilePath: CF514A.py
'''


def func():
    num = list(input().strip())
    base = [0, 1, 2, 3, 4, 4, 3, 2, 1, 0]
    init = 1 if num[0] == "9" else 0
    for i in range(init, len(num)):
        num[i] = str(base[int(num[i])])
    print("".join(num))


if __name__ == '__main__':
    func()
