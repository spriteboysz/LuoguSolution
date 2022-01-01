#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-02 23:25:05
LastEditTime: 2021-11-02 23:29:48
Description: 
FilePath: CF68A.py
'''


def func():
    *lst, a, b = map(int, input().strip().split())
    count = 0
    for i in range(a, b + 1):
        for item in lst:
            if i % item != i:
                break
        else:
            count += 1
    return count


if __name__ == '__main__':
    ans = func()
    print(ans)
