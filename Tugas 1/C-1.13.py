def myReverse(data):
    return [data[i] for i in range(len(data)-1, -1, -1)]

print(myReverse([2, 12, 4, 5, 6, 31, 9, 10]))
