#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-11 23:19:40
LastEditTime: 2021-12-12 16:12:38
Description: Bessie's Secret Pasture S
FilePath: P2666.py
'''


def func():
    n = int(input())
    count = 0
    for a in range(0, int(n ** 0.5) + 1):
        for b in range(0, int(n ** 0.5) + 1):
            if a * a + b * b > n:
                break
            for c in range(0, int(n ** 0.5) + 1):
                if a * a + b * b + c * c > n:
                    break
                for d in range(0, int(n ** 0.5) + 1):
                    if a * a + b * b + c * c + d * d > n:
                        break
                    if a * a + b * b + c * c + d * d == n:
                        count += 1
                        print(a, b, c, d)
                        break
    print(count)


if __name__ == '__main__':
    func()
