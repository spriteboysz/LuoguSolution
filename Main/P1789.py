#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-05 23:20:34
LastEditTime: 2021-12-05 23:41:01
Description: 【Mc生存】插火把
FilePath: P1789.py
'''


def func(): 
    n, m, k = map(int, input().strip().split())
    matrix = [[1] * n for _ in range(n)]
    torch, fluorite = [], []
    for _ in range(m):
        x, y = map(int, input().strip().split())
        for i in range(max(0, x - 1 - 2), min(n - 1, x - 1 + 2) + 1):
            for j in range(max(0, y - 1 - 2), min(n - 1, y - 1 + 2) + 1):
                pass

        
    for _ in range(k):
        x, y = map(int, input().strip().split())
        for i in range(max(0, x - 1 - 2), min(n - 1, x - 1 + 2) + 1):
            for j in range(max(0, y - 1 - 2), min(n - 1, y - 1 + 2) + 1):
                matrix[i][j] = 0
    
    print(matrix)

if __name__ == '__main__':
    func()
    