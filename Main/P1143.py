#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-31 10:46:05
LastEditTime: 2021-10-31 14:28:55
Description: 进制转换
FilePath: P1143.py
'''

import string


def func():
    n = int(input())
    sn = input().strip()
    m = int(input())

    base = list(string.digits + string.ascii_uppercase)
    # TODO：将n进制数转换成10进制数
    sd = 0
    for i in range(len(sn)):
        sd += base.index(sn[i]) * n ** (len(sn) - i - 1)

    # TODO: 将10进制数转换成m进制数
    sm = ""
    while sd > 0:
        sd, mod = divmod(sd, m)
        sm += base[mod]
    print(sm[::-1])


if __name__ == '__main__':
    func()
