#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-20 15:18:25
LastEditTime: 2021-11-20 22:08:37
Description: Anton and Polyhedrons
FilePath: CF785A.py
'''


def func():
    polyhedron = ["Tetrahedron", "Cube",
                  "Octahedron", "Dodecahedron", "Icosahedron"]
    face = [4, 6, 8, 12, 20]
    n = int(input())
    count = 0
    for _ in range(n):
        s = input().strip()
        count += face[polyhedron.index(s)]
    print(count)


if __name__ == '__main__':
    func()
