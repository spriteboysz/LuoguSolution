#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-31 14:56:56
LastEditTime: 2021-10-31 21:56:37
Description: 快速幂||取余运算
FilePath: P1226.py
'''

import time

def decorator(function):
    def inner():
        start = time.time()
        function()
        end = time.time()
        print("time: %f" % (end - start))
    return inner

@decorator
def func():
    a, b, p = map(int, input().strip().split())
    s = a ** b % p
    print("{}^{} mod {}={}".format(a, b, p, s))


if __name__ == '__main__':
    func()
