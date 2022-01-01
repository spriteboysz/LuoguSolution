#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-23 23:45:17
LastEditTime: 2021-10-24 00:06:14
Description: Car
FilePath: P6382.py
'''


def func():
    license = input().strip()
    city = license[:3]
    for item in license[3:]:
        if item.isdigit():
            digit = int(item)

    limited = [[1, 9], [2, 8], [3, 7], [4, 6], [5, 0]]
    lst = ["1"] * 5
    if city == "MDA":
        for i in range(5):
            if digit not in limited[i]:
                lst[i] = "0"

    print(" ". join(lst))


if __name__ == '__main__':
    func()
