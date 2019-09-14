def minmax(data):
    """Find the minimum and maximum values in the sequence of numbers."""
    a = len(data)
    max = data[0]
    min = data[0]
    for i in range(a):
        if max < data[i]:
            max = data[i]
        if min > data[i]:
            min = data[i]
    return (min,max)

print (minmax([1,2,4,5,7,8,10]))