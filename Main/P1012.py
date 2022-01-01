#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-28 23:00:47
LastEditTime: 2021-10-28 23:25:11
Description: 拼数
FilePath: P1012.py
'''


def func():
    n = int(input())
    lst = input().strip().split()

    # !自然数排序搞必定7 71这种场景，拼接排序实践
    for i in range(0, n):
        for j in range(i, n):
            if lst[i] + lst[j] < lst[j] + lst[i]:
                lst[i], lst[j] = lst[j], lst[i]
    print("".join(lst))


if __name__ == '__main__':
    func()
