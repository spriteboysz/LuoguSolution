#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-26 22:43:10
LastEditTime: 2021-10-26 22:57:21
Description: 肥胖问题
FilePath: P5714.py
'''


def func():
    m, n = map(float, input().strip().split())
    bmi = m / (n ** 2)
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 24:
        print("Normal")
    elif bmi >= 24:
        # TODO: 保留六位有效数字的写法
        print("%.6g" % bmi)
        print("Overweight")


if __name__ == '__main__':
    func()
