#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-23 23:07:19
LastEditTime: 2021-11-23 23:10:47
Description: Buy a Shovel
FilePath: CF732A.py
'''


def func():
    k, r = map(int, input().strip().split())
    for i in range(1, 11):
        if (k * i) % 10 == r or (k * i) % 10 == 0:
            print(i)
            break
    else:
        print(10)


if __name__ == '__main__':
    func()
    