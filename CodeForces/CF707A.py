#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-07 17:02:15
LastEditTime: 2021-11-07 17:08:53
Description: Brain's Photos
FilePath: CF707A.py
'''


def func():
    n, m = map(int, input().strip().split())
    photo = []
    for _ in range(n):
        photo.extend(input().strip().split())

    photo = list(set(photo))
    for color in ["C", "M", "Y"]:
        if color in photo:
            print("#Color")
            break
    else:
        print("#Black&White")


if __name__ == '__main__':
    func()
