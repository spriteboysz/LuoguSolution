# LuoguSolution

### 高精度
#### P1601 A + B Problem
```Python
def func():
    a, b = input().strip(), input().strip()
    if len(a) < len(b):
        a, b = b, a
    b = "0" * (len(a) - len(b)) + b

    # carry 进位标志
    carry, c = 0, ""
    for i in range(len(a) - 1, -1, -1):
        carry, mod = divmod(int(a[i]) + int(b[i]) + carry, 10)
        c = str(mod) + c
    print((str(carry) + c) if carry != 0 else c)
```
