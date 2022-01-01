#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-03 22:02:57
LastEditTime: 2021-11-03 22:07:45
Description: Helpful Maths
FilePath: CF339A.py
'''


def func():
    s = input().strip()
    numbers = list(map(str, sorted(s.split("+"))))
    return "+".join(numbers)


if __name__ == '__main__':
    ans = func()
    print(ans)
