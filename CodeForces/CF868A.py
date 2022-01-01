#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-13 23:05:46
LastEditTime: 2021-11-13 23:14:58
Description: Bark to Unlock
FilePath: CF868A.py
'''


def func():
    s = input().strip()
    flag1, flag2 = False, False
    n = int(input())
    for _ in range(n):
        t = input().strip() 
        if s == t:
            print("YES")
            break
        if t.startswith(s[1]):
            flag1 = True
        if t.endswith(s[0]):
            flag2 = True
        if flag1 and flag2:
            print("YES")
            break
    else:
        print("NO")


if __name__ == '__main__':
    func()
    