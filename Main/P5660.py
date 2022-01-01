#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-22 23:05:58
LastEditTime: 2021-10-22 23:12:31
Description: 数字游戏
FilePath: P5660.py
'''


def func():
    s = input().strip()
    return s.count("1")


if __name__ == '__main__':
    # !更改作题风格，调用主函数后打印结果，功能函数中仅return
    num = func()
    print(num)
    