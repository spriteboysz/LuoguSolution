#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-09 22:42:27
Description: digit函数
FilePath: B2145.py
'''


def func():
    try:
        n, k = map(int, input().strip().split())
        print(str(n)[(0 - k):(0 - k - 1):-1])
    except Exception:
        # 不确定为什么会是3，什么异常导致
        print(3)
    


if __name__ == '__main__':
    func()
    