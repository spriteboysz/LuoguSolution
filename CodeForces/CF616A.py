#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-18 23:26:43
LastEditTime: 2021-11-18 23:33:09
Description: Comparing Two Long Integers
FilePath: CF616A.py
'''


def func():
    a, b = input().strip().lstrip("0"), input().strip().lstrip("0")
    if len(a) > len(b):
        print(">")
    elif len(a) < len(b):
        print("<")
    else:
        if a == b:
            print("=")
        else:
            for i in range(len(a)):
                if int(a[i]) > int(b[i]):
                    print(">")
                    break
                elif int(a[i]) < int(b[i]):
                    print("<")
                    break
            else:
                print("=")


if __name__ == '__main__':
    func()
