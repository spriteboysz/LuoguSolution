#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-09-29 23:07:01
LastEditTime: 2021-09-29 23:37:50
Description: 求小数的某一位
FilePath: B2073.py
'''


def func():
    a, b, n = map(int, input().strip().split())
    num = a * 10 ** 10000 // b // (10 ** (10000 - n))
    print(num % 10)


if __name__ == '__main__':
    func()
