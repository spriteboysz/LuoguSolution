#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-09 23:32:13
Description: 
FilePath: B2121.py
'''

def func():
    word = input().strip().replace(",", " ").replace(".", " ").split()
    print(max(word, key = len))
    print(min(word, key = len))


if __name__ == '__main__':
    func()
    