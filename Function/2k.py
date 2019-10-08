from itertools import chain,combinations
while True:
    try:
        n = int(input('请输入牌的数量n（1<=n<=50）'))
    except:
        pass
    if type(n) == int and n <= 50 and n >= 1:
        break

list = []
while True:
    if len(list) < n:
        try:
            s = int(input('请输入牌的幂次数s（0<=s<=50）：'))
        except:
            pass
        list.append(2**s)
    if len(list)>=n:
        break

list = [2,5,7,8,9]
for i in len(list):





