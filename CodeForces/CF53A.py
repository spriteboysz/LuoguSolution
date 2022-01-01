#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-23 23:23:28
LastEditTime: 2021-11-23 23:27:49
Description: Autocomplete
FilePath: CF53A.py
'''


def func():
    inputted = input().strip()
    n = int(input())
    lst = []
    for _ in range(n):
        visited = input().strip()
        if visited.startswith(inputted):
            lst.append(visited)

    if len(lst) == 0:
        print(inputted)
    else:
        print(sorted(lst)[0])


if __name__ == '__main__':
    func()
