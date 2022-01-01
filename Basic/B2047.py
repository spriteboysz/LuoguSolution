#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-16 14:59:38
Description: 分段函数
FilePath: B2047.py
'''

def func():
    x = float(input())
    if 0 <= x < 5:
        y = 2.5 - x
    elif 5 <= x < 10:
        y = 2 - 1.5 * (x - 3) * (x - 3)
    elif 10 <= x < 20:
        y = x / 2 - 1.5
    else:
        pass

    print("%.3f" % y)


if __name__ == '__main__':
    func()
    
