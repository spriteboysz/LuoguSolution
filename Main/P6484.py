#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-25 22:28:34
LastEditTime: 2021-12-25 22:52:44
Description: ASTRO
FilePath: P6484.py
'''


from math import gcd


def func():
    star = []
    for _ in range(4):
        star.append(list(map(int, input().strip().split(":"))))
    start1, start2, interval1, interval2 = map(
        lambda el: el[0] * 60 + el[1], star)
    if abs(start1 - start2) % gcd(interval1, interval2) != 0:
        print("Never")
    else:
        while start1 != start2:
            if(start1 < start2):
                start1 += interval1
            else:
                start2 += interval2
                
        day, hour = divmod(start2, 24 * 60)
        hour, minutes = divmod(hour, 60)
        week = ["Saturday", "Sunday", "Monday", "Tuesday",
                "Wednesday", "Thursday", "Friday"]
        print(week[day % 7])
        print("%02d:%02d" % (hour, minutes))


if __name__ == '__main__':
    func()
