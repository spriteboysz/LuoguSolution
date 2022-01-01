#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-23 23:43:19
LastEditTime: 2021-12-23 23:54:17
Description: 保龄球
FilePath: P1918.py
'''


def func():
    n = int(input())
    bowling = list(map(int, input().strip().split()))
    dic = {v: i + 1 for i, v in enumerate(bowling)}
    q = int(input())
    for _ in range(q):
        num = int(input())
        if num in dic.keys():
            print(dic[num])
        else:
            print(0)


if __name__ == '__main__':
    func()
