def sum_odd_squares(n):
    sum_odd_squares = sum(k*k for k in range(n) if k%2 == 1)
    return sum_odd_squares

print(sum_odd_squares(4))
sums = [2 ** k for k in range(0,9)]
print(sums)
print()