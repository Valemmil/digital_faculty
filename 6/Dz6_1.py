"""
1. Последний с четными
Дано: список (list) целых чисел (int).

Задание: нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд), затем перемножить эту сумму
и последний элемент исходного массива.
"""


def main():
    in_num = input("Введите список целых чисел через пробел: ")
    if in_num != "":
        elements = in_num.split(" ")
    else:
        elements = "0"
    result = 0

    for i in elements[::2]:
        result += int(i)
    result *= int(elements[-1])
    print("Результат: " + str(result))


if __name__ == "__main__":
    main()
