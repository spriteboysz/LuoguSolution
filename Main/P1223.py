#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-06 23:35:22
LastEditTime: 2021-12-06 23:52:31
Description: 排队接水
FilePath: P1223.py
'''


def func():
    n = int(input())
    time = list(map(int, input().strip().split()))
    queue = []
    for i in range(n):
        queue.append([i + 1, time[i]])
    queue = sorted(queue, key=lambda el: el[1])

    total = 0
    sequence = []
    for i, v in enumerate(queue):
        sequence.append(str(v[0]))
        total += v[1] * (n - 1 - i)
    print(" ".join(sequence))
    print("%.2f" % (total/n))


if __name__ == '__main__':
    func()
