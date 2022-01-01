#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-30 22:46:04
LastEditTime: 2021-12-30 22:52:58
Description: PATULJCI
FilePath: P6314.py
'''


def func():
    dwarf = []
    for _ in range(9):
        dwarf.append(int(input()))
    total = sum(dwarf)
    for i in range(len(dwarf) - 1):
        for j in range(i + 1, len(dwarf)):
            if dwarf[i] + dwarf[j] == total - 100:
                dwarf.pop(j)
                dwarf.pop(i)
                print("\n".join(map(str, dwarf)))
                return


if __name__ == '__main__':
    func()
