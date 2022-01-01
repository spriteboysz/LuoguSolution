#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-12 23:29:09
LastEditTime: 2021-11-12 23:42:29
Description: Ksusha and Array
FilePath: CF299A.py
'''


def func():
    n = int(input())
    num = list(set(map(int, input().strip().split())))
    for i in range(len(num)):
        for j in range(len(num)):
            if num[j] % num[i] != 0:
                break
        else:
            return num[i]
    return -1
    

if __name__ == '__main__':
    ans = func()
    print(ans)
    