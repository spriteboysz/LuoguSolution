#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-09 23:20:29
Description: 最高分数的学生姓名
FilePath: B2125.py
'''


def func():
    n = int(input())
    score, name = [0] * n, ["0"] * n
    for i in range(n):
        score[i], name[i] = input().strip().split()

    score = list(map(int, score))
    print(name[score.index(max(score))])


if __name__ == '__main__':
    func()
    