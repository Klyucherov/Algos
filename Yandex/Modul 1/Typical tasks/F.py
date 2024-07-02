'''
Научиться определять дуликаты

Использование встроенных функций и модулей (collections.Counter):
Использование Counter из модуля collections, чтобы подсчитать количество вхождений каждого элемента.


from collections import Counter

lst = [1, 2, 3, 4, 1, 2, 5]
counter = Counter(lst)
duplicates = [item for item, count in counter.items() if count > 1]

print(duplicates)  # [1, 2]

'''

from collections import Counter


def solutionF(nums):
    counter = Counter(nums)
    duplicates = [item for item, count in counter.items() if count > 1]

    return duplicates


n = 5
nums = '3 1 3 4 2'.split()
print(solutionF(nums))
