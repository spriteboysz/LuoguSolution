#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-01 23:09:07
LastEditTime: 2021-11-01 23:31:59
Description: Triangle
FilePath: CF6A.py
'''


def func():
    lst = list(sorted(map(int, input().strip().split())))
    ans = "IMPOSSIBLE"
    for i in range(0, len(lst) - 2):
        for j in range(i + 1, len(lst) - 1):
            for k in range(j + 1, len(lst)):
                if lst[i] + lst[j] > lst[k]:
                    return "TRIANGLE"   
                elif lst[i] + lst[j] == lst[k]:
                    if ans != "TRIANGLE":
                        ans = "SEGMENT"

    return ans


if __name__ == '__main__':
    ans = func()
    print(ans)
