#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-01 15:46:56
LastEditTime: 2022-01-01 16:15:35
Description: Alice Wins! (easy version)
FilePath: P7939.py
'''


def func():
    base1 = {"2": "1", "3": "2", "1": "3"}
    base2 = {"1": "2", "2": "3", "3": "1"}
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().strip().split()
        b = input().strip().split()
        for i in range(n):
            a[i] = base1[b[i]]
        for i in range(n, 2 * n):
            b[i] = base2[a[i]]
        s = str(2 * n) + "\n"
        s += " ".join(a) + "\n"
        s += " ".join(b)
        print(s)


if __name__ == '__main__':
    func()
