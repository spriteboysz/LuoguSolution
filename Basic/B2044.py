"""
题目描述
给出一名学生的语文、数学、英语成绩，判断他是否恰好有一门课不及格（成绩小于 6060 分）。若该学生恰好有一门成绩不及格输出 11，否则输出 00。

输入格式
一行包含三个 0 \sim 1000∼100 之间的整数，分别表示该生的语文、数学、英语成绩。

输出格式
该学生恰好有一门成绩不及格输出 11，否则输出 00。
"""
num = []
num = input().split(" ")
sum = 0
for item in num:
    if int(item) < 60:
        sum += 1
if sum == 1:
    print("1")
else:
    print("0")
