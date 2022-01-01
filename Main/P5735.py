#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-24 17:25:36
LastEditTime: 2021-10-24 17:30:26
Description: 距离函数
FilePath: P5735.py
'''


def dis(ax, ay, bx, by):
    return ((bx - ax) ** 2 + (by - ay) ** 2) ** 0.5

def func():
    # *题目示例的输入格式有问题
    ax, ay = map(float, input().strip().split())
    bx, by = map(float, input().strip().split())
    cx, cy = map(float, input().strip().split())

    ab = dis(ax, ay, bx, by)
    ac = dis(ax, ay, cx, cy)
    bc = dis(bx, by, cx, cy)

    print("%.2f" % (ab + ac + bc))
    

if __name__ == '__main__':
    func()