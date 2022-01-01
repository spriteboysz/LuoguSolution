#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-28 16:21:09
LastEditTime: 2021-11-28 16:33:10
Description: Rock-paper-scissors
FilePath: CF48A.py
'''


def func():
    gesture = []
    for _ in range(3):
        gesture.append(input().strip())
        
    if gesture.count("rock") == 2 and gesture.count("paper") == 1:
        result = gesture.index("paper")
    elif gesture.count("paper") == 2 and gesture.count("scissors") == 1:
        result = gesture.index("scissors")
    elif gesture.count("scissors") == 2 and gesture.count("rock") == 1:
        result = gesture.index("rock")
    else:
        result = 3
    print(["F", "M", "S", "?"][result])
    


if __name__ == '__main__':
    func()
    