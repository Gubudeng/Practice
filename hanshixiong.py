n = int(input())
m = int(input())
n_A = ''
m_B = ''
# 产生n+m长的字符串
str = ''

for i in range(n):
    n_A += 'A'

for i in range(m):
    m_B += 'B'

if n_A == 'AAA':
    print("错误")
elif m_B == 'BBB':
    print("错误")
else:
    str = n_A + m_B
print(str)