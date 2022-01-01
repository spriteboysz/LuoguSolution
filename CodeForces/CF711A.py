#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-07 17:33:44
LastEditTime: 2021-11-07 17:49:33
Description: Bus to Udayland
FilePath: CF711A.py
'''


def func():
    n = int(input())
    seats = []
    flag = False
    for _ in range(n):
        row = input().strip()
        if flag == False and "OO" in row:
            flag = True
            # *仅匹配第一个"OO"
            row = row.replace("OO", "++", 1)
        seats.append(row)
    if flag:
        print("YES")
        print("\n".join(seats))
    else:
        print("NO")


if __name__ == '__main__':
    func()
