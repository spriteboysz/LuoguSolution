#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-29 22:11:58
LastEditTime: 2021-12-29 22:32:41
Description: 排队
FilePath: P5412.py
'''


def func():
    t = int(input())
    for _ in range(t):
        boy, girl = [], []
        _ = int(input())
        gender = list(map(int, input().strip().split()))
        student = input().strip().split()
        for g, s in zip(gender, student):
            boy.append(s) if g == 1 else girl.append(s)
        print(" ".join(sorted(girl)))
        print(" ".join(sorted(boy)))


if __name__ == '__main__':
    func()
