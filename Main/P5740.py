#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-10 22:17:52
LastEditTime: 2021-10-10 22:45:07
Description: 最厉害的学生
FilePath: P5740.py
'''

def func():
    n = int(input())
    lst = []
    # !总和应比最小值还要小
    ssum = -1
    for i in range(n):
        row = input().strip().split()
        total = sum(map(int, row[1:]))
        if total > ssum:
            ssum = total
            lst = row
    
    print(" ".join(lst))
    


if __name__ == '__main__':
    func()
    