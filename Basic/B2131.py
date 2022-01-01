#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-21 23:09:48
LastEditTime: 2021-10-21 23:24:38
Description: 甲流病人初筛
FilePath: B2131.py
'''


def func():
    n = int(input())

    lst = []
    for _ in range(n):
        name, temperature, cough = input().strip().split()
        if float(temperature) >= 37.5 and int(cough) == 1:
            print(name)
            lst.append(name)

    # !空字符串情况下会多输出一个换行
    #print("\n".join(lst))
    print(len(lst))


if __name__ == '__main__':
    func()
