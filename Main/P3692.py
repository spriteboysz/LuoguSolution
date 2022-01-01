#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-28 22:53:09
LastEditTime: 2021-12-28 23:40:39
Description: 夏幻的考试
FilePath: P3692.py
'''


def func():
    t, n = map(int, input().strip().split())
    answer = list(input().strip())

    for _ in range(t):
        identification = input().strip()
        type1 = "A" if identification[-1] == "0" else "B"
        identification = int(identification, base=2)
        type2 = input().strip()
        ans = []
        for _ in range(n):
            s = input().strip()
            if s.count("1") == 1:
                ans.append(chr(s.index("1") + 65))
            else:
                ans.append(0)

        if 1 <= identification <= 10000:
            print("ID: %d" % identification)

            if type2 == "10" and type1 == "A" or type2 == "01" and type1 == "B":
                print("Type Correct")
            else:
                print("Type Incorrect")

            point = sum(map(lambda el1, el2: 1 if el1 ==
                        el2 else 0, answer, ans)) * 100 / n
            print("%.1f" % point)
        else:
            print("Wrong ID")

        print()


if __name__ == '__main__':
    func()
