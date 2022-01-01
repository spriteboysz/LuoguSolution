#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-29 23:18:49
LastEditTime: 2021-10-30 00:09:43
Description: 多项式输出
FilePath: P1067.py
'''


def func():
    n = int(input())
    lst = list(map(int, input().strip().split()))

    polynome = ""
    for index, element in enumerate(lst):
        if element != 0:
            if element == 1 and index != n:
                element = ""
            if element == -1 and index != n:
                element = "-"
            
            if index == n:
                polynome += str(element) + "+"
            elif index == n - 1:
                polynome += str(element) + "x" + "+"
            else:
                polynome += str(element) + "x^" + str(n - index) + "+"

    print(polynome[0:-1].replace("+-", "-"))


if __name__ == '__main__':
    func()
