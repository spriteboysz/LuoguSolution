#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-04 00:06:14
LastEditTime: 2021-11-26 23:00:44
Description: Shell Game
FilePath: CF35A.py
'''


def func():
    with open('input.txt', 'r') as f:
        init = int(f.readline())
        lst = [0] * 4
        lst[init] = 1
        for _ in range(3):
            a, b = map(int, f.readline().strip().split())
            lst[a], lst[b] = lst[b], lst[a]
            
    with open('output.txt', 'w') as f:
        f.write(str(lst.index(1)))


if __name__ == '__main__':
    func()
