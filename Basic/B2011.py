"""
题目描述
两个整数 aa 和 bb 分别作为分子和分母，既分数 a/ba/b，求它的浮点数值（双精度浮点数，保留小数点后 99 位）。

输入格式
输入仅一行，包括两个整数 aa 和 bb。

输出格式
输出也仅一行，分数 a/ba/b 的浮点数值（双精度浮点数，保留小数点后 99 位）。
"""
# num = []
# num = input().split(" ")
# print('%.9f' % (int(num[0])/int(num[1])))

a = input().split(" ")
b = input().split(" ")
ax,ay = float(a[0]),float(a[1])
bx,by = float(b[0]),float(b[1])
l = ((ax-bx)**2+(ay-by)**2)**0.5
print("%.3f" % l)

# 给定一个整数 NN，判断其正负。如果 N>0N>0, 输出 positive ; 如果 N=0N=0, 输出 zero ; 如果 N<0,N<0, 输出 negative。
num = int(input())
if num == 0:
    print("zero")
elif num > 0:
    print("positive")
else:
    print("negative")