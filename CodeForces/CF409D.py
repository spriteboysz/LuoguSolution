#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-04 23:33:34
LastEditTime: 2021-11-04 23:36:42
Description: 
FilePath: CF409D.py
'''


def func():
    ans = [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0]
    return ans[int(input()) - 1]


if __name__ == '__main__':
    ans = func()
    print(ans)
