#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-09-29 22:28:18
LastEditTime: 2021-09-29 22:45:51
Description: 计算星期几
FilePath: B2074.py
'''


def func():
    a, b = map(int, input().strip().split())
    week = ["Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"]
    print(week[(a ** b) % 7])


if __name__ == '__main__':
    func()
