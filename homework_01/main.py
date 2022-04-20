"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers, power=2):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    <<< power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num ** power for num in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    if number in [1, 0]:
        return 0
    for i in range(2, number):
        if number % i == 0:
            return 0
    return number


def filter_numbers(numbers, types):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    <<< filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    <<< filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if types is EVEN:
        return list(filter(lambda x: x % 2 == 0, numbers))
    elif types is ODD:
        return list(filter(lambda x: x % 2 == 1, numbers))
    elif types is PRIME:
        return list(filter(lambda x: x != 0, map(is_prime, numbers)))



