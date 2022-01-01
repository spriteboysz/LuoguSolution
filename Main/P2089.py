#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-04 23:27:11
LastEditTime: 2021-12-05 15:49:00
Description: 烤鸡
FilePath: P2089.py
'''


def func():
    n = int(input())
    count = 0
    lst = []
    for i1 in range(1, 4):
        for i2 in range(1, 4):
            for i3 in range(1, 4):
                for i4 in range(1, 4):
                    for i5 in range(1, 4):
                        for i6 in range(1, 4):
                            for i7 in range(1, 4):
                                for i8 in range(1, 4):
                                    for i9 in range(1, 4):
                                        for i10 in range(1, 4):
                                            if i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9 + i10 == n:
                                                count += 1
                                                lst.append([i1, i2, i3, i4, i5,
                                                            i6, i7, i8, i9, i10])
    print(count)
    for item in lst:
        print(" ".join(map(str, item)))


if __name__ == '__main__':
    func()
