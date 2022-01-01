#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-24 17:35:39
LastEditTime: 2021-10-24 17:37:43
Description: 
FilePath: P7257.py
'''


def func():
    numbers = input().strip().split()
    print(max(int(numbers[0][::-1]), int(numbers[1][::-1])))


if __name__ == '__main__':
    func()
