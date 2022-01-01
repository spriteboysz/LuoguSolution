#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-16 15:19:22
Description: 收集瓶盖赢大奖
FilePath: B2041.py
'''


def func():
    lucky, encourage = map(int, input().strip().split())

    if lucky >= 10 or encourage >= 20:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    func()
