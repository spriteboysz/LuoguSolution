#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-18 23:12:04
LastEditTime: 2021-12-18 23:46:33
Description: Gerrymandering
FilePath: P7886.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().strip().split())
        if (n * m) % k != 0:
            print("NO")
        else:
            print("YES")
            lst = sum([[str(i)] * k for i in range(1, n * m // k + 1)], [])
            for i in range(n):
                if i % 2 == 0:
                    print(" ".join(lst[(m * i):(m * i + m)]))
                else:
                    print(" ".join(lst[(m * i):(m * i + m)][::-1]))


if __name__ == '__main__':
    func()
