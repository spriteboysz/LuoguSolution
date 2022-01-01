#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-23 22:51:27
LastEditTime: 2021-12-23 22:54:14
Description: 合并序列
FilePath: P1628.py
'''


def func():
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input().strip())
    t = input().strip()
    print("\n".join(sorted(filter(lambda el: el.startswith(t), words))))


if __name__ == '__main__':
    func()
