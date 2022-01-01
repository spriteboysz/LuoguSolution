#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-06 22:45:12
Description: ISBN号码
FilePath: P1055.py
'''


def func():
    isbn = input().strip()
    nums, verf1 = "".join(isbn.split("-", 2)).split("-")

    count = 0
    for i in range(len(nums)):
        count += int(nums[i]) * (i + 1)
        
    verf2 = "X" if count % 11 == 10 else str(count % 11)
    if verf2 == verf1:
        print("Right")
    else:
        print(isbn[:-1] + verf2)


if __name__ == '__main__':
    func()
