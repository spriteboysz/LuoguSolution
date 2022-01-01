#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-29 22:15:57
LastEditTime: 2021-10-29 22:48:36
Description: 统计数字
FilePath: P1097.py
'''


def func():
    n = int(input())

    dic = {}
    for _ in range(n):
        key = int(input())
        if key not in dic.keys():
            dic[key] = 1
        else:
            dic[key] += 1
    # TODO:字典排序按key返回列表
    for i in sorted(dic):
        print(i, dic[i])


if __name__ == '__main__':
    func()
