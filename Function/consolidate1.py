def is_multiple(n,m):
    """It is judged whether n is an integral multiple of m.

    data   n and m are entered as integers.

    factor if n is an integral multiple of m, the output is True, otherwise is Fale.
    """
    if n%m == 0:
        return True
    else:
        return False

# 注意不可以用判断类型来做，需要转换思路，从余数入手做，因为如果用判断类型做，python中的除法得出的类型都是float类型。
print(6/3)
print(6//3)
print(3//6)
print(is_multiple(6, 3))
print(is_multiple(3, 6))