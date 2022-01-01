#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-23 23:14:03
LastEditTime: 2021-11-23 23:20:43
Description: Bar
FilePath: CF56A.py
'''


def func():
    n = int(input())
    alcohol = ["ABSINTH", "BEER", "BRANDY", "CHAMPAGNE", "GIN",
               "RUM", "SAKE", "TEQUILA", "VODKA", "WHISKEY", "WINE"]
    count = 0
    for _ in range(n):
        visitor = input().strip()
        if visitor.isdigit():
            if int(visitor) < 18:
                count += 1
        else:
            if visitor in alcohol:
                count += 1
    print(count)


if __name__ == '__main__':
    func()
