#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-30 23:33:27
LastEditTime: 2021-10-31 00:04:04
Description: 分数线划定
FilePath: P1068.py
'''


def func():
    n, m = map(int, input().strip().split())
    volunteers = []
    for _ in range(n):
        id, point = map(int, input().strip().split())
        volunteers.append([id, point])
    # *二级排序（一级降序，二级升序），排序关键字取负数
    volunteers = sorted(volunteers, key=lambda el: (
        el[1], -el[0]), reverse=True)
    last = int(m * 1.5) - 1
    volunteers = list(
        filter(lambda el: el[1] >= volunteers[last][1], volunteers))

    print(volunteers[last][1], len(volunteers))
    for i in range(len(volunteers)):
        print(volunteers[i][0], volunteers[i][1])


if __name__ == '__main__':
    func()
