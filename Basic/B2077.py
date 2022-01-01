#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-16 21:45:40
Description: 角谷猜想
FilePath: B2077.py
'''


def func():
    num = int(input())
    while num > 1:
        if num % 2 == 1:
            num = num * 3 + 1
            print("%d*3+1=%d" % ((num-1)/3, num))
        else:
            num /= 2
            print("%d/2=%d" % (num*2, num))
    print("End")


if __name__ == '__main__':
    func()
