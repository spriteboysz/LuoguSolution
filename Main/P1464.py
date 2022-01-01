#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-05 16:00:46
LastEditTime: 2021-12-05 16:55:31
Description: Function
FilePath: P1464.py
'''

lst, ret = [], []


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return 1048576
    elif [a, b, c] in lst:
        return ret[lst.index([a, b, c])]
    elif a < b < c:
        ans = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else:
        ans = w(a - 1, b, c) + w(a - 1, b - 1, c) + \
            w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    ret.append(ans)
    lst.append([a, b, c])
    return ans


def func():
    while True:
        a, b, c = map(int, input().strip().split())        
        if a == b == c == -1:
            break
        else:
            print("w(%d, %d, %d) = %d" % (a, b, c, w(a, b, c)))


if __name__ == '__main__':
    func()
