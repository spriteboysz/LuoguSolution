#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2021-10-14 23:25:07
LastEditTime: 2021-10-15 22:14:41
Description: 斯诺登的密码
FilePath: P1603.py
"""


def func():
    pwd = input().strip().split()
    notebook = "zero one two three four five six seven eight \
    nine ten eleven twelve thirteen fourteen fifteen sixteen \
    seventeen eighteen nineteen twenty"
    notebook = list(notebook.split())
    notebook[1] = (notebook[1] + " a another first").split()
    notebook[2] = (notebook[2] + " second both").split()
    notebook[3] = (notebook[3] + " third").split()

    key = [0]
    for item in pwd:
        for i in range(len(notebook)):
            if item in notebook[i]:
                key.append(i ** 2 % 100)
                break

    key = sorted(key)
    s = ""
    for item in key:
        s += "%02d" % item
    if s.lstrip("0") == "":
        print("0")
    else:
        print(s.lstrip("0"))


if __name__ == "__main__":
    func()
