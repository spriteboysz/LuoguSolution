#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-10 13:23:55
LastEditTime: 2021-10-12 00:16:48
Description: 压缩技术
FilePath: P1319.py
'''


def func():
    lst1 = list(map(int, input().strip().split()))
    num = lst1.pop(0)

    lst2 = []
    flag = -1
    for item in lst1:
        lst2.append(str(flag) * item)
        flag = 0 - flag

    lst2 = "".join(lst2).replace("-1", "0")
    for i in range(num * num):
        print(lst2[i], end="")
        if (i + 1) % 7 == 0:
            print()
        


if __name__ == '__main__':
    func()
