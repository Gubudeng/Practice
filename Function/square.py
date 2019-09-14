from time import *
def sumsquare(n):
    """Calculate the sum of the squares of 1~n."""
    sq = 0
    for i in range(n):
        sq += (i+1) **2
    return sq

# begin_time = time()
# for i in range(1000000):
#     print(sumsquare(12))
# end_time = time()
# run_time = end_time - begin_time
# print(run_time)

squares = [k*k for k in range(1, 13)]
print(squares)
factors = [k for k in range(1,13) if 12%k == 0]
print(factors)

sumsquares = sum(k*k for k in range(1,13))
begin_time = time()
for i in range(1000000):
    print(sumsquares)
end_time = time()
run_time = end_time - begin_time
print(run_time)