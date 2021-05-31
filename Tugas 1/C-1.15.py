from typing import List

def areDistinct(data: List[int]) -> bool:
    uniqueNums = {x for x in data}
    return len(uniqueNums) == len(data)

data1 = [1, 2, 9, 8, 5, 10]
data2 = [2, 4, 2, 8, 12, 6]

print(areDistinct(data1))
print(areDistinct(data2))
