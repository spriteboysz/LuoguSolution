#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-24 23:04:34
LastEditTime: 2021-10-25 23:07:15
Description: 表达式括号匹配
FilePath: P1739.py
'''


def func():
    try:
        s = input().strip()
    except:
        print("NO")
        return
    brackets = ""
    for item in s:
        if item == "@":
            break
        if item == "(" or item == ")":
            brackets += item

    while "()" in brackets:
        brackets = brackets.replace("()", "")
    if len(brackets) == 0:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    func()
