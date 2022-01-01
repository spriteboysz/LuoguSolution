#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-30 21:35:46
LastEditTime: 2021-10-30 21:38:59
Description: 高低位交换
FilePath: P1100.py
'''


def func():
    n = int(input())
    binary = bin(n).replace("0b", "").zfill(32)
    print(int(binary[16:] + binary[:16], 2))


if __name__ == '__main__':
    func()
