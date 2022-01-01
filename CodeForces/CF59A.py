#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-03 00:09:25
LastEditTime: 2021-11-03 00:13:50
Description: Word
FilePath: CF59A.py
'''


def func():
    s = input().strip()
    lowers, uppers = 0, 0
    for item in s:
        if item.islower():
            lowers += 1
        else:
            uppers += 1

    return s.upper() if uppers > lowers else s.lower()


if __name__ == '__main__':
    ans = func()
    print(ans)