#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-26 23:59:28
LastEditTime: 2021-10-27 22:21:17
Description: 小D与笔试
FilePath: P5601.py
'''


def func():
    n, q = map(int, input().strip().split())
    questions = []
    for _ in range(n):
        row = input().strip().split()
        questions.append(row)
    # TODO:字典初始化的一种方式，嵌套列表转字典
    questions = dict(questions)

    for _ in range(q):
        # TODO：赋值的新方式，变量+列表同时赋值
        question, *options = input().strip().split()
        print(chr(options.index(questions[question]) + 65))


if __name__ == '__main__':
    func()
