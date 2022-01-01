#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-04 23:38:45
LastEditTime: 2021-11-04 23:44:38
Description: 
FilePath: CF409C.py
'''


def func():
    lst = list(map(int, input().strip().split()))
    recipe = [1, 1, 2, 7, 4]
    return min(map(lambda x, y: x//y, lst, recipe))


if __name__ == '__main__':
    ans = func()
    print(ans)
