#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-24 16:17:34
LastEditTime: 2021-12-17 00:03:23
Description: 最急救助
FilePath: P6565.py
'''


def func():
    n = int(input())
    sos = []
    for _ in range(n):
        name = input().strip()
        info = input().strip()
        count = 0
        for i in range(len(info) - 2):
            if info[i] == "s" and info[i + 1] == "o" and info[i + 2] == "s":
                count += 1
        sos.append([name, count])
    maximum = max(sos, key=lambda el: el[1])[1]
    names = []
    for el in filter(lambda el: el[1] == maximum, sos):
        names.append(el[0])
    print(" ".join(names))
    print(maximum)


if __name__ == '__main__':
    func()
