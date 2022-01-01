#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-27 21:42:07
LastEditTime: 2021-11-27 21:51:09
Description: Letter
FilePath: CF43B.py
'''


def func():
    s1 = input().strip()
    s2 = input().strip().replace(" ", "")
    key = list(set(s2))
    count = list(map(lambda el: s2.count(el), key))
    for i in range(len(key)):
        if s1.count(key[i]) < count[i]:
            print("NO")
            break
    else:
        print("YES")


if __name__ == '__main__':
    func()
