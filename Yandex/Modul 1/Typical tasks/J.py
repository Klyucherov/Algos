from collections import Counter

def solutionJ(n, nums):
    count = Counter(nums)
    for key, value in count.items():
        if value != 2:
            return key
        

n = 5
nums = '4 1 2 1 2'.split()
nums2 = '42 67 67 42 42'.split(' ')

print(solutionJ(n, nums))

print(solutionJ(n, nums2))



# Доп решение
'''
Можно предложить более быстрое и оптимальное решение для этой задачи,
использующее свойства битовой операции XOR. Операция XOR обладает полезным свойством,
что если применить её к двум одинаковым числам, то результатом будет ноль (а XOR a = 0).
Если применить XOR ко всем числам в массиве, то все пары
одинаковых чисел аннулируются, и останется только одно число, которое встречается один раз.

'''
def find_unique(nums):
    unique_num = 0
    for num in nums:
        unique_num ^= num
    return unique_num

# Примеры использования
n = 5
nums1 = list(map(int, '4 1 2 1 2'.split()))
nums2 = list(map(int, '42 67 67 42 42'.split()))

print(find_unique(nums1))  # Вывод: 4
print(find_unique(nums2))  # Вывод: 42