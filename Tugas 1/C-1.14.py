from typing import List

def isProductOdd(data):
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if (data[i] != data[j]) and ((data[i] * data[j]) % 2 == 1):
                return data[i], data[j]
    return False

def isProductOddOptimized(data):
    oddElements = {x for x in data if x % 2 == 1}
    if len(oddElements) > 1:
        return oddElements.pop(), oddElements.pop()
    return False

data1 = [1, 3, 10, 2, 12]
data2 = [10, 12, 18, 6, 8]

print(isProductOdd(data1))
print(isProductOddOptimized(data2))
