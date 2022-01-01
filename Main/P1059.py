#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-10 23:37:30
LastEditTime: 2021-10-10 23:41:46
Description: 明明的随机数
FilePath: P1059.py
'''


def func():
    num = int(input())
    lst = list(map(int, input().strip().split()))
    print(len(set(lst)))
    print(" ".join(map(str, sorted(list(set(lst))))))


if __name__ == '__main__':
    func()
