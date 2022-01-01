#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-07 22:56:48
LastEditTime: 2021-12-07 23:09:59
Description: 陶陶摘苹果（升级版）
FilePath: P1478.py
'''


def func():
    n, s = map(int, input().strip().split())
    a, b = map(int, input().strip().split())
    apple = []
    for _ in range(n):
        x, y = map(int, input().strip().split())
        if x <= a + b:
            apple.append([x, y])
    apple = sorted(apple, key=lambda el: el[1])
    current, count = 0, 0
    for el in apple:
        if current + el[1] <= s:
            current += el[1]
            count += 1
        else:
            break
    print(count)


if __name__ == '__main__':
    func()
