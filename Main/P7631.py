#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-14 23:18:00
LastEditTime: 2021-12-14 23:28:46
Description: GLJIVE
FilePath: P7631.py
'''


def func():
    gold = []
    for _ in range(10):
        gold.append(int(input()))
    total, ans = 0, 0
    for i in range(10):
        total += gold[i]
        if abs(ans - 100) > abs(total - 100):
            ans = total
        if abs(ans - 100) == abs(total - 100):
            ans = max(ans, total)
        if total > 100:
            break
    print(ans)


if __name__ == '__main__':
    func()
