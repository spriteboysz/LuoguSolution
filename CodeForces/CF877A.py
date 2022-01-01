#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-08 23:14:07
LastEditTime: 2021-11-28 17:12:17
Description: Alex and broken contest
FilePath: CF877A.py
'''


def func():
    problem = input().strip()
    count = 0
    for name in ["Danil", "Olya", "Slava", "Nikita", "Ann"]:
        count += problem.count(name)
        
    print("YES" if count == 1 else "NO")


if __name__ == '__main__':
    func()
