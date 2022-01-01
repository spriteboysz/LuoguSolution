#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-05 22:34:32
LastEditTime: 2021-11-05 22:36:39
Description: Borze
FilePath: CF32B.py
'''


def func():
    s = input().strip()
    print(s.replace("--", "2").replace("-.", "1").replace(".", "0"))


if __name__ == '__main__':
    func()
    