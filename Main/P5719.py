#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-07 23:04:49
Description: 分类平均
FilePath: P5719.py
'''


def func():
    n, k = map(int, input().strip().split())
    lst1, lst2 = [], []
    for i in range(1, n + 1):
        if i % k == 0:
            lst1.append(i)
        else:
            lst2.append(i)

    print("%.1f %.1f" % (sum(lst1)/len(lst1), sum(lst2)/len(lst2)))


if __name__ == '__main__':
    func()
