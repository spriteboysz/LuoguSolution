#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-02 23:09:16
LastEditTime: 2021-11-02 23:12:45
Description: Is your horseshoe on the other hoof? 
FilePath: CF228A.py
'''


def func():
    horseshoes = list(map(int, input().strip().split()))
    return 4 - len(set(horseshoes))


if __name__ == '__main__':
    ans = func()
    print(ans)
