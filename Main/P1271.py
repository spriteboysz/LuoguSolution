#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-10 23:07:27
LastEditTime: 2021-10-10 23:11:00
Description: 选举学生会
FilePath: P1271.py
'''

def func():
    n, m = map(int, input().strip().split())
    lst = map(int, input().strip().split())
    print(" ".join(map(str, sorted(lst))))

if __name__ == '__main__':
    func()
    