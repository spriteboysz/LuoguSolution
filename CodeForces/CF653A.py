#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-06 22:54:59
LastEditTime: 2021-11-06 23:06:26
Description: Bear and Three Balls
FilePath: CF653A.py
'''


def func():
    _ = int(input())
    balls = sorted(list(set(map(int, input().strip().split()))))

    for i in range(2, len(balls)):
        if balls[i - 2] + 2 == balls[i - 1] + 1 == balls[i]:
            print("YES")
            break
    else:
        print("NO")


if __name__ == '__main__':
    func()
