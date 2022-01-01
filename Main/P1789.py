#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-05 23:20:34
LastEditTime: 2022-01-01 23:39:02
Description: 【Mc生存】插火把
FilePath: P1789.py
'''


def func():
    torch = [[-2, 0], [2, 0], [0, 2], [0, -2],
             [-1, -1], [-1, 0], [-1, 1],
             [0, -1], [0, 0], [0, 1],
             [1, -1], [1, 0], [1, 1]]
    fluorite = [[-2, -2], [-2, -1], [-2, 0], [-2, 1], [-2, 2],
                [-1, -2], [-1, -1], [-1, 0], [-1, 1], [-1, 2],
                [0, -2], [0, -1], [0, 0], [0, 1], [0, 2],
                [1, -2], [1, -1], [1, 0], [1, 1], [1, 2],
                [2, -2], [2, -1], [2, 0], [2, 1], [2, 2]]
    n, m, k = map(int, input().strip().split())
    matrix = [[1] * (n + 4) for _ in range(n + 4)]
    for _ in range(m):
        x, y = map(lambda el: int(el) - 1 + 2, input().strip().split())
        for item in torch:
            matrix[x + item[0]][y + item[1]] = 0

    for _ in range(k):
        x, y = map(lambda el: int(el) - 1 + 2, input().strip().split())
        for item in fluorite:
            matrix[x + item[0]][y + item[1]] = 0

    count = 0
    for row in range(2, 2 + n):
        count += matrix[row][2:2 + n].count(1)
    print(count)


if __name__ == '__main__':
    func()
