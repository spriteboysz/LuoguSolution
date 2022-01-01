#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-17 23:20:02
LastEditTime: 2021-11-17 23:27:55
Description: Diverse Team
FilePath: CF988A.py
'''


def func():
    _, k = map(int, input().strip().split())
    lst = list(map(int, input().strip().split()))
    if len(set(lst)) < k:
        print("NO")
    else:
        print("YES")
        index = []
        for item in list(set(lst))[0: k]:
            index.append(str(lst.index(item) + 1))
        print(" ".join(index))


if __name__ == '__main__':
    func()
