def phone_combinations(digits):
    # Словарь отображающий цифры на соответствующие буквы
    digit_to_char = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    # Проверяем, если входная строка пуста
    if not digits:
        return []

    # Рекурсивная функция для генерации комбинаций
    def backtrack(index, path):
        # Если длина текущего пути равна длине входной строки, добавляем путь к результатам
        if index == len(digits):
            combinations.append(''.join(path))
            return
        # Получаем соответствующие буквы для текущей цифры
        possible_letters = digit_to_char[digits[index]]
        for letter in possible_letters:
            path.append(letter)  # Добавляем букву в текущий путь
            backtrack(index + 1, path)  # Рекурсивный вызов для следующей цифры
            path.pop()  # Удаляем букву для возврата к предыдущему состоянию

    combinations = []
    backtrack(0, [])
    return combinations


# Пример использования
input_string1 = "23"
input_string2 = "92"

output_string1 = ' '.join(phone_combinations(input_string1))
output_string2 = ' '.join(phone_combinations(input_string2))

print(f"Input: {input_string1} -> Output: {output_string1}")
print(f"Input: {input_string2} -> Output: {output_string2}")
