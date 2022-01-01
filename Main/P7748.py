#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-28 23:57:33
LastEditTime: 2021-12-29 22:06:38
Description: VOLIM
FilePath: P7748.py
'''


def func():
    k, n = int(input()), int(input())
    answer = []
    for _ in range(n):
        time, type = input().strip().split()
        answer.append([int(time), type])
    count = 0
    for i, v in enumerate(answer):
        count += answer[i][0]
        if count <= 210:
            if answer[i][1] == "T":
                k += 1
        else:    
            break
    if k % 8 == 0:
        print(8)
    else:
        print(k % 8)


if __name__ == '__main__':
    func()
