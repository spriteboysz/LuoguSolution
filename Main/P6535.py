#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-25 22:06:46
LastEditTime: 2021-12-25 22:26:03
Description: TRENER
FilePath: P6535.py
'''


def func():
    n = int(input())
    dic = {}
    for _ in range(n):
        word = input().strip()[0]
        if word in dic.keys():
            dic[word] += 1
        else:
            dic[word] = 1
    lst = []
    for k, v in dic.items():
        if v >= 5:
            lst.append(k)
    print("PREDAJA" if len(lst) == 0 else "".join(sorted(lst)))


if __name__ == '__main__':
    func()
