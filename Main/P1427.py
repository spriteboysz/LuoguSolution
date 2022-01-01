#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-09-25 21:49:34
LastEditTime: 2021-09-25 22:04:42
Description: 小鱼的数字游戏
FilePath: P1427.py
'''


def func():
    lst1 = list(map(int, input().strip().split()))
    lst2 = []
    for i in range(lst1.index(0) - 1, -1, -1):
        lst2.append(str(lst1[i]))
    
    print(" ".join(lst2))



if __name__ == '__main__':
    func()
