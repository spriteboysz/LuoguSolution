#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-29 22:33:23
LastEditTime: 2021-12-29 22:38:07
Description: 头像上传
FilePath: P5315.py
'''


def func():
    n, l, g = map(int, input().strip().split())
    for _ in range(n):
        w, h = map(int, input().strip().split())
        while w > g or h > g:
            w, h = w // 2, h // 2
        if w < l or h < l:
            print("Too Young")
        elif w != h:
            print("Too Simple")
        elif w == h:
            print("Sometimes Naive")


if __name__ == '__main__':
    func()
