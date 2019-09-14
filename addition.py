print("请输入两个数字(q退出)")
while True:
    a = input()
    b = input()
    if a == 'q':
        break
    try:
        c = float(a) + float(b)
    except ValueError:
        print("输入有误")
    else:
        print(c)