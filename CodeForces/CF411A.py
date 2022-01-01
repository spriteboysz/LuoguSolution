#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-04 23:08:26
LastEditTime: 2021-11-04 23:17:07
Description: 
FilePath: CF411A.py
'''


def func():
    complexity = [False] * 4
    password = input().strip()
    if len(password) >= 5:
        complexity[0] = True
    else:
        return "Too weak"
    
    for item in password:
        if all(complexity):
            return "Correct"
        if item.isupper():
            complexity[1] = True
        elif item.islower():
            complexity[2] = True
        elif item.isdigit():
            complexity[3] = True
    return "Too weak"


if __name__ == '__main__':
    ans = func()
    print(ans)
