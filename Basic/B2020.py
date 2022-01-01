#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-09-26 22:48:55
LastEditTime: 2021-09-26 22:59:39
Description: 分糖果
FilePath: B2020.py
'''

def func():
    lst = list(map(int, input().strip().split()))
    
    count = 0 
    for i in range(len(lst)):
        count += lst[i] % 3
        each = lst[i] // 3
        lst[i] = each
        lst[i - 1] += each
        try:
            lst[i + 1] += each
        except IndexError:
            lst[0] += each
            
    print(" ".join(map(str,lst)))
    print(count)


if __name__ == '__main__':
    func()
    