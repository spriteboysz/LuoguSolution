#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-10 13:20:02
LastEditTime: 2021-10-12 23:13:55
Description: 蛇形方阵
FilePath: P5731.py
'''

# *第一个生成器函数*


def count(n):
    for i in range(1, n * n + 1):
        yield i


def circle(lst, a, b, num):
    # right
    for j in range(a, b + 1):
        lst[a][j] = next(num)
    # down
    for i in range(a + 1, b + 1):
        lst[i][b] = next(num)
    # left
    for j in range(b - 1, a - 1, -1):
        lst[b][j] = next(num)
    # up
    for i in range(b - 1, a, -1):
        lst[i][a] = next(num)


def func():
    n = int(input())
    # 初始化二维数组
    lst = []
    for i in range(n):
        lst.append([0] * n)

    num = count(n)
    # circle函数可以画圈
    for i in range(0, (n + 1) // 2):
        circle(lst, i, n - i - 1, num)

    # 循环输出二维数组
    for i in range(n):
        for j in range(n):
            print("%3d" % lst[i][j], end="")
        print()


if __name__ == '__main__':
    func()
