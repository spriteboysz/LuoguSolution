#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-02 17:34:28
LastEditTime: 2022-01-02 17:49:57
Description: TIMSKO
FilePath: P6443.py
'''


def func():
    m, n, k = map(int, input().strip().split())
    for i in range((m + n - k) // 3 + 1, -1, -1):
        girl, boy = m - i * 2, n - i
        if boy + girl >= k and boy >= 0 and girl >= 0:
            print(i)
            break
    else:
        print(0)


if __name__ == '__main__':
    func()
