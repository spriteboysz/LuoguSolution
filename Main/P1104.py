#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-29 22:58:56
LastEditTime: 2021-10-29 23:15:39
Description: 生日
FilePath: P1104.py
'''


def func():
    num = int(input())
    students = []
    for _ in range(num):
        name, *birthday = input().strip().split()
        students.append([name, birthday])
    # 后输入的同学先输出，将列表逆序
    students = students[::-1]
    # TODO： 元组推导式tuple()?生成器表达式？
    # !按整数比较，非字典序 
    students = sorted(students, key=lambda el: tuple(int(item)
                      for item in el[1]))
    for i in range(num):
        print(students[i][0])


if __name__ == '__main__':
    func()
