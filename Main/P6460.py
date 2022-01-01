#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-25 23:11:16
LastEditTime: 2021-12-25 23:30:50
Description: NATRIJ
FilePath: P6460.py
'''


def func():
    time = []
    for _ in range(2):
        time.append(list(map(int, input().strip().split(":"))))
    start, end = map(lambda el: el[0] * 3600 + el[1] * 60 + el[2], time)

    interval = end - start + 24 * 3600
    if interval % (24 * 3600) == 0:
        print("24:00:00")
    else:
        hour, interval = divmod(interval, 3600)
        minute, second = divmod(interval, 60)
        print("%02d:%02d:%02d" % (hour % 24, minute, second))


if __name__ == '__main__':
    func()
