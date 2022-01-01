#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-06 15:02:43
Description: 三角形分类
FilePath: P5717.py
'''

def func():
    a, b, c = sorted(list(map(int, input().strip().split())))
    if a + b <= c:
        print("Not triangle")
    else:
        if a * a + b * b == c * c:
            print("Right triangle")
        if a * a + b * b > c * c:
            print("Acute triangle")
        if a * a + b * b < c * c:
            print("Obtuse triangle")
        if a == b:
            print("Isosceles triangle")
        if a == b == c:
            print("Equilateral triangle")

if __name__ == '__main__':
    func()
    
