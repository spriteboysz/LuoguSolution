#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-03 23:25:49
LastEditTime: 2022-01-03 23:54:37
Description: 
FilePath: P2925.py
'''


def func():
    c, h = map(int, input().strip().split())
    v = []
    for _ in range(h):
        v.append(int(input()))
    for i in range(h):
        for j in range(c, -1, -1):
            

    
    # for (i=1;i<=n;i++)
    #     {
    #         for (j=m;j>=a[i];j--)
    #         f[j]=max(f[j],f[j-a[i]]+a[i]);
    #         if (f[m]==m) {printf("%d",m); return 0;}//优化，如果已经达到最好的结果（装满），就直接退掉
    #     }
    #     printf("%d",f[m]);


if __name__ == '__main__':
    func()
    