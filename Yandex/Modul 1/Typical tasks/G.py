from collections import Counter

def solutionG(one, two):
    if Counter(one) == Counter(two):
        print(Counter(one))
        print(Counter(two))
        return True
    else: return False
    
        
        
a = 'мошкара'
b = 'ромашка'

print(solutionG(a, b))

a = 'кошка'
b = 'лошка'

print(solutionG(a, b))



# Еще пример

def are_anagrams(word1, word2):
    # Приведение к нижнему регистру для регистронезависимого сравнения
    word1 = word1.lower()
    word2 = word2.lower()
    
    # Сортировка букв в каждом слове
    sorted_word1 = ''.join(sorted(word1))
    sorted_word2 = ''.join(sorted(word2))
    
    # Сравнение отсортированных строк
    return sorted_word1 == sorted_word2

# Примеры использования
word1 = input().strip()
word2 = input().strip()

print(are_anagrams(word1, word2))
