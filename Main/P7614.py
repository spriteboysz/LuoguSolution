#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-27 23:38:05
LastEditTime: 2021-10-28 22:56:33
Description: NAJBOLJIH 5 
FilePath: P7614.py
'''


def func():
    lst1 = []
    for _ in range(8):
        lst1.append(int(input()))

    lst2 = sorted(lst1)
    total, lst3 = 0, []
    for i, element in enumerate(lst1):
        if element not in lst2[:3]:
            total += element
            lst3.append(str(i + 1))
    print(total)
    print(" ".join(lst3))


if __name__ == '__main__':
    func()
