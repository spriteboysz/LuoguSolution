#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-10 22:48:00
LastEditTime: 2021-10-10 22:59:03
Description: 歌唱比赛
FilePath: P5738.py
'''


def func():
    n, m = map(int, input().strip().split())
    mmax = -1
    for i in range(n):
        row = list(map(int, input().strip().split()))
        avg = (sum(row) - max(row) - min(row)) / (m - 2)
        if avg > mmax:
            mmax = avg

    print("%.2f" % mmax)


if __name__ == '__main__':
    func()
