# Первое решение
def solutionA(n: int, p1: list , p2: list) -> str: 
    txt = ''
    for i in range(n):
        txt += str(p1[i])+ ' '
        txt += str(p2[i])+ ' '
 
    return txt
    

n = 3
p1 = '1 2 3'
p2 = '4 5 6'

new_p1 = list(map(int, p1.split()))
new_p2 = list(map(int, p2.split()))

print(solutionA(n, new_p1, new_p2))


# Второе решение
from itertools import chain

def main():
    with open('input.txt') as f:
        _ = f.readline()  # Пропускаем первую строку
        rus = f.readline().split()  # Считываем российские композиции
        foreign = f.readline().split()  # Считываем зарубежные композиции
        mix = chain(*zip(rus, foreign))  # Создаем смешанный плейлист
        print(" ".join(mix))  # Выводим результат

if __name__ == "__main__":
    main()
